import logging
from typing import List

from grammar.DecafParser import DecafParser
from grammar.DecafVisitor import DecafVisitor
from .constants import get_constant
class CodeGenVisitor(DecafVisitor):
    def __init__(self, symbol_table):
        super().__init__()
        self.logger = logging.getLogger("CodeGenVisitor")
        self.logger.setLevel(logging.ERROR)
        self.logger.handlers = []
        self.logger.handlers.clear()
        self.logger.propagate = False
        
        # Add a single console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(levelname)s:%(name)s: %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        self.tempCounter = 0
    
        self.memory_allocations = []

        self.symbol_table = symbol_table
        self.indentation = 0
        self.output = []
        # Add includes at the beginning of the file
        self.output.extend([
            "#include <stdio.h>",
            "#include <stdlib.h>",
            "#include <stdbool.h>",
            "#include <math.h>",
            "#include \"array_wrapper.h\"",
            "",
            "// Forward declarations",
            ""
        ])
    
    def visitGoal(self, ctx: DecafParser.GoalContext):
        # Generate forward declarations for all classes
        self.logger.debug("visitGoal started.")
        self.generateForwardDeclarations(ctx)

        # First, generate all class struct definitions
        self.logger.debug("visitGoal: generating class struct definitions")
        for class_decl in ctx.classDeclaration():
            class_name = class_decl.Identifier(0).getText()
            parent_class = None
            if len(class_decl.Identifier()) > 1:
                parent_class = class_decl.Identifier(1).getText()
            
            # Generate struct for class
            self.emit(f"typedef struct {class_name} {{")
            self.indentation += 1
            
            # If class extends another, include parent's fields first
            if parent_class:
                self.emit(f"// Inherited fields from {parent_class}")
                self.emit(f"{parent_class} parent;  // Parent class fields")
            
            # Generate fields
            for field in class_decl.fieldDeclaration():
                self.visit(field)
            
            # Add vtable pointer if needed
            if class_decl.methodDeclaration() or parent_class:
                self.emit(f"struct {class_name}_vtable *vptr;")
            
            self.indentation -= 1
            self.emit(f"}} {class_name};")
            self.emit("")

        # Then, generate all vtable structs
        self.logger.debug("visitGoal: generating vtable structs")
        for class_decl in ctx.classDeclaration():
            if class_decl.methodDeclaration() or len(class_decl.Identifier()) > 1:
                self.generateStructs(class_decl)

        # Finally, generate constructors and method implementations
        self.logger.debug("visitGoal: generating method implementations")
        for class_decl in ctx.classDeclaration():
            parent_class = None
            if len(class_decl.Identifier()) > 1:
                parent_class = class_decl.Identifier(1).getText()
            self.generateConstructor(class_decl, parent_class)
            for method in class_decl.methodDeclaration():
                self.visit(method)
                self.emit("")

        # Visit main class last
        self.logger.debug("visitGoal: visiting main class.")
        self.visit(ctx.mainClass())
        
        return "\n".join(self.output)
    
    def visitMainClass(self, ctx: DecafParser.MainClassContext):
        # In C, we just need the main function
        self.emit("int main(int argc, char *argv[]) {")
        self.indentation += 1
        
        # Visit the statement in main method
        self.logger.debug("visitMainClass: visiting statement.")
        self.visit(ctx.statement())
        self.freeMemory()

        # Add return statement
        self.emit("return 0;")
        self.indentation -= 1
        self.emit("}")
        self.emit("")
    
    def visitClassDeclaration(self, ctx: DecafParser.ClassDeclarationContext):
        class_name = ctx.Identifier(0).getText()
        parent_class = None
        
        self.logger.debug(f"visitClassDeclaration: visiting class {class_name}")
        
        # Check if class extends another class
        if len(ctx.Identifier()) > 1:
            parent_class = ctx.Identifier(1).getText()
            self.logger.debug(f"Class {class_name} extends {parent_class}")
        
        # Generate struct for class
        self.emit(f"typedef struct {class_name} {{")
        self.indentation += 1
        
        # If class extends another, include parent's fields first
        if parent_class:
            self.emit(f"// Inherited fields from {parent_class}")
            self.emit(f"{parent_class} parent;  // Parent class fields")
        
        # Generate fields
        self.logger.debug(f"visitClassDeclaration: visiting fields")
        for field in ctx.fieldDeclaration():
            self.visit(field)
        
        # Add vtable pointer if needed
        self.logger.debug(f"visitClassDeclaration: emitting {class_name}_vtable *vptr;")
        if ctx.methodDeclaration() or parent_class:
            self.emit(f"struct {class_name}_vtable *vptr;")
        
        self.indentation -= 1
        self.emit(f"}} {class_name};")
        self.emit("")
        
        # Generate vtable if class has methods or inherits methods
        self.logger.debug(f"visitClassDeclaration: generate method structs")
        if ctx.methodDeclaration() or parent_class:
            self.generateStructs(ctx)
        
        # Generate constructor function for all classes
        self.generateConstructor(ctx, parent_class)
    
        # Generate methods
        self.logger.debug(f"visitClassDeclaration: visiting and generating methods.")
        for method in ctx.methodDeclaration():
            self.visit(method)
            self.emit("")
    
    def generateConstructor(self, ctx: DecafParser.ClassDeclarationContext, parent_class: str = None):
        class_name = ctx.Identifier(0)
        self.logger.debug(f"Generating constructor for class {class_name}")
        constructor_name = get_constant("init_function_name") 
        # Generate constructor function declaration
        self.emit(f"int {class_name}{constructor_name}({class_name}* this) {{")
        self.indentation += 1
        
        # If there's a parent class, call parent's constructor
        if parent_class:
            self.emit(f"// Initialize parent class fields")
            self.emit(f"{parent_class}{constructor_name}(({parent_class}*)this);")
        
        # Initialize vtable pointer
        if ctx.methodDeclaration() or parent_class:
            self.emit(f"// Initialize vtable")
            self.emit(f"static struct {class_name}_vtable vtable = {{")
            self.indentation += 1
            
            # Add function pointers
            for method in ctx.methodDeclaration():
                method_name = method.Identifier().getText()
                self.emit(f".{method_name} = {class_name}_{method_name},")
            
            self.indentation -= 1
            self.emit("};")
            self.emit(f"this->vptr = &vtable;")
        
        # Return success
        self.emit("return 0;")
        self.indentation -= 1
        self.emit("}")
        self.emit("")
    
    def generateStructs(self, ctx: DecafParser.ClassDeclarationContext):
        class_name = ctx.Identifier(0).getText()
        parent_class = None
        if len(ctx.Identifier()) > 1:
            parent_class = ctx.Identifier(1).getText()
        
        self.emit(f"struct {class_name}_vtable {{")
        self.indentation += 1
        
        # Include parent class methods if inheriting
        if parent_class:
            self.logger.debug(f"Including methods from parent class {parent_class}")
            self.emit(f"// Inherited methods from {parent_class}")
            # Include all methods from parent class's vtable
            self.emit(f"struct {parent_class}_vtable parent;  // Parent class methods")
            self.emit("")
            self.emit(f"// Methods defined in {class_name}")
        # Generate function pointers for each method
        for method in ctx.methodDeclaration():
            return_type = self.visit(method.type_())
            if return_type is None:
                self.logger.error(f"None return type detected at {ctx.start.line}")
                continue
            method_name = method.Identifier().getText()
            
            # Generate parameter list
            params = [f"{class_name}*"]
            if method.parameterList():
                param_types = [self.visit(param.type_()) for param in method.parameterList().parameter()]
                params.extend(param_types)
            
            self.emit(f"{return_type} (*{method_name})({', '.join(params)});")
        
        self.indentation -= 1
        self.emit("};")
        self.emit("")
    
    def visitType(self, ctx: DecafParser.TypeContext):
        token_type = ctx.getText()
        type_map = {
            'int':'int',
            'boolean': 'bool',
            'void': 'void',
            'int[]': 'ArrayWrapper*',
            'String': 'char*',
            'String[]': 'char**'
        }
        # if it;s not in the map, its non-primitive and needs a pointer.
        return type_map.get(token_type, token_type + "*")
    
    def visitMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        class_name = ctx.parentCtx.Identifier(0).getText()
        method_name = ctx.Identifier().getText()
        self.logger.debug(f"visitMethodDeclaration: Processing method {class_name}_{method_name}")
        
        return_type = self.visit(ctx.type_())
        self.logger.debug(f"visitMethodDeclaration: Return type is {return_type}")

        # Generate function declaration with class instance as first parameter
        params = [f"{class_name}* this"]
        if ctx.parameterList():
            params.extend(self.visit(ctx.parameterList()))
        self.logger.debug(f"visitMethodDeclaration: Parameters are {params}")
        
        self.emit(f"{return_type} {class_name}_{method_name}({', '.join(params)}) {{")
        self.indentation += 1

        # Visit method body
        if ctx.methodBody():
            self.logger.debug(f"visitMethodDeclaration: Processing method body for {class_name}.{method_name}")
            self.visit(ctx.methodBody())

        self.indentation -= 1
        self.emit("}")

    def visitParameterList(self, ctx: DecafParser.ParameterListContext) -> List[str]:
        params = []
        for param in ctx.parameter():
            param_type = self.visit(param.type_())
            param_name = param.Identifier().getText()
            params.append(f"{param_type} {param_name}")
        return params

    def visitMethodBody(self, ctx: DecafParser.MethodBodyContext):
        self.logger.debug("visitMethodBody: Processing local declarations")
        # Visit local declarations
        for local_decl in ctx.localDeclaration():
            self.visit(local_decl)

        self.logger.debug("visitMethodBody: Processing statements")
        # Visit statements
        for stmt in ctx.statement():
            self.visit(stmt)

        # Visit return expression
        self.logger.debug("visitMethodBody: Processing return expression")
        if not ctx.RETURN() or not ctx.expression():
            self.logger.error("visitMethodBody: Missing return token or expression")
            return
        return_expr = self.visit(ctx.expression())
        self.logger.debug(f"visitMethodBody: Return expression evaluated to: {return_expr}")
        if return_expr is None:
            self.logger.error("visitMethodBody: Return expression evaluated to None")
            return
        
        self.emit(f"return {return_expr};")
  
    def visitVarDeclaration(self, ctx: DecafParser.VarDeclarationContext):
        var_type = self.visit(ctx.type_())
        
        var_name = ctx.Identifier().getText()
        self.emit(f"{var_type} {var_name};")

    def visitVariableAssignmentStatement(self, ctx: DecafParser.VariableAssignmentStatementContext):
        var_name = ctx.Identifier().getText()
        expression = self.visit(ctx.expression())
        
        # Get the current class scope from the context
        class_scope = ctx.parentCtx
        while class_scope and not isinstance(class_scope, DecafParser.ClassDeclarationContext):
            class_scope = class_scope.parentCtx
            
        # If we're in a class scope
        if class_scope and isinstance(class_scope, DecafParser.ClassDeclarationContext):
            class_name = class_scope.Identifier(0).getText()
            var_name = self.build_access_chain(var_name, class_name)
        
        self.emit(f"{var_name} = {expression};")

    def visitIfElseStatement(self, ctx: DecafParser.IfElseStatementContext):
        self.logger.debug("Enter if Statement")
        condition = self.visit(ctx.expression())
        self.emit(f"if ({condition}) {{")
        self.indentation += 1
        self.visit(ctx.ifBlock())
        self.indentation -= 1
        if ctx.elseBlock():
            self.emit("} else {")
            self.indentation += 1
            self.visit(ctx.elseBlock())
            self.indentation -= 1
        self.emit("}")
    def visitArrayAssignmentStatement(self, ctx: DecafParser.ArrayAssignmentStatementContext):
        var_name = ctx.Identifier().getText()
        index = self.visit(ctx.expression(0))
        value = self.visit(ctx.expression(1))
        
        # Get the current class scope from the context
        class_scope = ctx.parentCtx
        while class_scope and not isinstance(class_scope, DecafParser.ClassDeclarationContext):
            class_scope = class_scope.parentCtx
            
        # If we're in a class scope
        if class_scope and isinstance(class_scope, DecafParser.ClassDeclarationContext):
            class_name = class_scope.Identifier(0).getText()
            var_name = self.build_access_chain(var_name, class_name)
        
        self.emit(f"{var_name}->data[{index}] = {value};")
    
    def visitPrintStatement(self, ctx: DecafParser.StatementContext):
        expr = self.visit(ctx.expression())
        self.emit(f"printf(\"%d\\n\", {expr});")

    def visitExpressionStatement(self, ctx: DecafParser.StatementContext):
        expr = self.visit(ctx.expression(0))
        self.emit(f"{expr};")

    def visitIntLitExpression(self, ctx: DecafParser.IntLitExpressionContext):
        self.logger.debug(f"Visiting integer literal expression: {ctx.getText()}")
        value = ctx.IntegerLiteral().getText()
        return value

    def visitEqExpression(self, ctx: DecafParser.EqExpressionContext):
        self.logger.debug(f"Visiting equality expression: {ctx.getText()}")
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        return f"{l} == {r}"

    def visitArrayAccessExpression(self, ctx: DecafParser.ArrayAccessExpressionContext) -> str:
        self.logger.debug("Visiting array access expression")
        array = self.visit(ctx.expression(0))
        index = self.visit(ctx.expression(1))
        return f"*array_at({array}, {index})"

    def visitArrayLengthExpression(self, ctx: DecafParser.ArrayLengthExpressionContext) -> str:
        self.logger.debug("Visiting array length expression")
        array = self.visit(ctx.expression())
        return f"array_length({array})"

    def visitMethodCallExpression(self, ctx: DecafParser.MethodCallExpressionContext) -> str:
        self.logger.debug("Visiting method call expression")
        obj = self.visit(ctx.expression(0))
        method = ctx.Identifier().getText()
        args = [obj]
        if len(ctx.expression()) > 1:
            args.extend([self.visit(expr) for expr in ctx.expression()[1:]])
        return f"{obj}->vptr->{method}({', '.join(args)})"

    def visitNotExpression(self, ctx: DecafParser.NotExpressionContext) -> str:
        self.logger.debug("Visiting NOT expression")
        expr = self.visit(ctx.expression())
        return f"!{expr}"

    def visitArrayInstantiationExpression(self, ctx: DecafParser.ArrayInstantiationExpressionContext) -> str:
        self.logger.debug("Visiting array instantiation expression")
        size = self.visit(ctx.expression())
        return f"create_array({size})"

    def visitObjectInstantiationExpression(self, ctx: DecafParser.ObjectInstantiationExpressionContext) -> str:
        self.logger.debug("Visiting object instantiation expression")
        class_name = ctx.Identifier().getText()
        temp_var = self.getTempVar()
        constructor_name = get_constant("init_function_name")
        self.memory_allocations.append(temp_var)
        self.emit(f"{class_name}* {temp_var} = ({class_name}*)malloc(sizeof({class_name})) ;")
        self.emit(f"{class_name}{constructor_name}({temp_var});")
        return temp_var

    def visitPowExpression(self, ctx: DecafParser.PowExpressionContext) -> str:
        self.logger.debug("Visiting power expression")
        base = self.visit(ctx.expression(0))
        exp = self.visit(ctx.expression(1))
        # Check if both operands are integer literals
        if base.isdigit() and exp.isdigit():
            return str(pow(int(base), int(exp)))
        return f"pow({base}, {exp})"

    def visitMulExpression(self, ctx: DecafParser.MulExpressionContext) -> str:
        self.logger.debug("Visiting multiplication expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        # Check if both operands are integer literals
        if left.isdigit() and right.isdigit():
            return str(int(left) * int(right))
        return f"{left} * {right}"

    def visitAddExpression(self, ctx: DecafParser.AddExpressionContext) -> str:
        self.logger.debug("Visiting addition expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        # Check if both operands are integer literals
        if left.isdigit() and right.isdigit():
            return str(int(left) + int(right))
        return f"{left} + {right}"

    def visitSubExpression(self, ctx: DecafParser.SubExpressionContext) -> str:
        self.logger.debug("Visiting subtraction expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        # Check if both operands are integer literals
        if left.isdigit() and right.isdigit():
            return str(int(left) - int(right))
        return f"{left} - {right}"

    def visitLtExpression(self, ctx: DecafParser.LtExpressionContext) -> str:
        self.logger.debug("Visiting less than expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return f"{left} < {right}"

    def visitAndExpression(self, ctx: DecafParser.AndExpressionContext) -> str:
        self.logger.debug("Visiting AND expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return f"{left} && {right}"

    def visitBooleanLitExpression(self, ctx: DecafParser.BooleanLitExpressionContext) -> str:
        self.logger.debug("Visiting boolean literal expression")
        return ctx.BooleanLiteral().getText().lower()

    def build_access_chain(self, var_name: str, class_name: str) -> str:
        """Helper method to build the access chain for struct member access."""
        found, parent_chain = self.is_class_field(var_name, class_name)
        if found:
            access_chain = "this"
            for parent in parent_chain:
                if isinstance(parent, str) and parent.startswith("."):
                    access_chain += parent  # Use dot notation for direct struct access
                else:
                    access_chain += "->"+parent  # Use arrow for pointer access
            return f"{access_chain}->{var_name}"
        return var_name

    def visitIdentifierExpression(self, ctx: DecafParser.IdentifierExpressionContext) -> str:
        self.logger.debug("Visiting identifier expression")
        var_name = ctx.Identifier().getText()
        
        # Get the current class scope from the context
        class_scope = ctx.parentCtx
        while class_scope and not isinstance(class_scope, DecafParser.ClassDeclarationContext):
            class_scope = class_scope.parentCtx
            
        # If we're in a class scope
        if class_scope and isinstance(class_scope, DecafParser.ClassDeclarationContext):
            class_name = class_scope.Identifier(0).getText()
            return self.build_access_chain(var_name, class_name)
        
        return var_name


    def visitWhileStatement(self, ctx: DecafParser.WhileStatementContext):
        self.logger.debug("Enter while statement")
        condition = self.visit(ctx.expression())
        if condition is None:
            self.logger.error(f"Invalid while condition at {ctx.start.line}")

        self.emit(f"while ({condition}) {{")
        self.indentation += 1
        self.visit(ctx.whileBlock())
        self.indentation -= 1
        self.emit("}")


    def is_class_field(self, var_name: str, class_name: str) -> tuple[bool, list[str]]:
        """
        Check if an identifier `var` is in the class scope and return the chain of parent classes if found
        Returns: (found, parent_chain)
        """
        if var_name in self.symbol_table[f"global.{class_name}"]:
            # its in the scope of current class
            return True, []
            
        parent = self.symbol_table['global'].get(class_name).parent_class
        if parent:
            found, parent_chain = self.is_class_field(var_name, parent)
            if found:
                # Use dot notation for parent field access
                return True, ["parent"] if not parent_chain else ["parent"] + ["." + p for p in parent_chain]
        return False, []

    def visitThisExpression(self, ctx: DecafParser.ThisExpressionContext) -> str:
        self.logger.debug("Visiting this expression")
        return "this"

    def visitParenExpression(self, ctx: DecafParser.ParenExpressionContext) -> str:
        self.logger.debug("Visiting parenthesized expression")
        expr = self.visit(ctx.expression())
        return f"({expr})"
    

    def _get_expression_list(self, expressions) -> List[str]:
        return [self.visit(expr) for expr in expressions]

    def generateForwardDeclarations(self, ctx: DecafParser.GoalContext):
        # Forward declare all classes as structs first
        self.emit("// Forward declarations for all classes")
        for class_decl in ctx.classDeclaration():
            class_name = class_decl.Identifier(0).getText()
            self.emit(f"typedef struct {class_name} {class_name};")
        self.emit("")
        
        # Forward declare vtable structs
        self.emit("// Forward declarations for vtable structs")
        for class_decl in ctx.classDeclaration():
            class_name = class_decl.Identifier(0).getText()
            if class_decl.methodDeclaration() or len(class_decl.Identifier()) > 1:
                self.emit(f"struct {class_name}_vtable;")
        self.emit("")
        
        # Forward declare all methods
        self.emit("// Forward declarations for all methods")
        for class_decl in ctx.classDeclaration():
            class_name = class_decl.Identifier(0).getText()
            # Add forward declarations for all methods
            for method in class_decl.methodDeclaration():
                return_type = self.visit(method.type_())
                method_name = method.Identifier().getText()
                params = [f"{class_name}* this"]
                if method.parameterList():
                    param_types = [f"{self.visit(param.type_())} {param.Identifier().getText()}" 
                                 for param in method.parameterList().parameter()]
                    params.extend(param_types)
                self.emit(f"{return_type} {class_name}_{method_name}({', '.join(params)});")
            
            # Add forward declaration for init function
            constructor_name = get_constant("init_function_name")
            self.emit(f"int {class_name}{constructor_name}({class_name}* this);")
        self.emit("")
    
    def indent(self) -> str:
        return "    " * self.indentation
    
    def emit(self, code: str):
        self.output.append(self.indent() + code)
    
    def getTempVar(self):
        self.tempCounter += 1
        return f"__tempvar{self.tempCounter}"

    def freeMemory(self):
        for var in self.memory_allocations: 
            self.emit(f"// free({var});")
            self.emit(f"// {var} = NULL;")
        self.memory_allocations = []