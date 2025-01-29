import logging
from typing import List

from grammar.DecafParser import DecafParser
from grammar.DecafVisitor import DecafVisitor

class CodeGenVisitor(DecafVisitor):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("CodeGenVisitor")
        self.logger.setLevel(logging.DEBUG)
        self.logger.handlers = []
        self.logger.handlers.clear()
        self.logger.propagate = False
        
        # Add a single console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(levelname)s:%(name)s: %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        
        self.indentation = 0
        self.output = []
        # Add includes at the beginning of the file
        self.output.extend([
            "#include <stdio.h>",
            "#include <stdlib.h>",
            "#include <stdbool.h>",
            "",
            "// Forward declarations",
            ""
        ])
    
    def visitGoal(self, ctx: DecafParser.GoalContext):
        # Generate forward declarations for all classes
        self.logger.debug("visitGoal started.")
        self.generateForwardDeclarations(ctx)
        
        # Visit main class first
        self.logger.debug("visitGoal: visiting main class.")
        self.visit(ctx.mainClass())
        
        # Visit all other class declarations
        self.logger.debug("visitGoal: visiting class declarations")
        for class_decl in ctx.classDeclaration():
            self.visit(class_decl)
        
        return "\n".join(self.output)
    
    def visitMainClass(self, ctx: DecafParser.MainClassContext):
        # In C, we just need the main function
        self.emit("int main(int argc, char *argv[]) {")
        self.indentation += 1
        
        # Visit the statement in main method
        self.logger.debug("visitMainClass: visiting statement.")
        self.visit(ctx.statement())
        
        # Add return statement
        self.emit("return 0;")
        self.indentation -= 1
        self.emit("}")
        self.emit("")
    
    def visitClassDeclaration(self, ctx: DecafParser.ClassDeclarationContext):
        class_name = ctx.Identifier(0).getText()
        
        self.logger.debug(f"visitClassDeclaration: visiting class {class_name}")
        
        # Generate struct for class
        self.emit(f"typedef struct {class_name} {{")
        self.indentation += 1
        
        # Generate fields
        self.logger.debug(f"visitClassDeclaration: visiting fields")
        for field in ctx.fieldDeclaration():
            self.visit(field)
        
        # Add vtable pointer if needed
        self.logger.debug(f"visitClassDeclaration: emitting {class_name}_vtable *vptr;")
        if ctx.methodDeclaration():
            self.emit(f"struct {class_name}_vtable *vptr;")
        
        self.indentation -= 1
        self.emit(f"}} {class_name};")
        self.emit("")
        
        # Generate vtable if class has methods
        self.logger.debug(f"visitClassDeclaration: generate method method structs")
        if ctx.methodDeclaration():
            self.generateStructs(ctx)
        
        # Generate methods
        self.logger.debug(f"visitClassDeclaration: visiting and generating methods.")
        for method in ctx.methodDeclaration():
            self.visit(method)
            self.emit("")
    
    def generateStructs(self, ctx: DecafParser.ClassDeclarationContext):
        class_name = ctx.Identifier(0).getText()
        self.emit(f"struct {class_name}_vtable {{")
        self.indentation += 1
        
        # Generate function pointers for each method
        for method in ctx.methodDeclaration():
            return_type = self.visit(method.type_())
            if return_type == None:
                print(ctx.start)
                # raise "None return type detected"
            method_name = method.Identifier().getText()
            self.emit(f"{return_type} (*{method_name})({class_name}*, ...);")
        
        self.indentation -= 1
        self.emit("};")
        self.emit("")
    
    def visitType(self, ctx: DecafParser.TypeContext):
        type = ctx.getText()
        type_map = {
            'int':'int',
            'boolean': 'bool',
            'void': 'void',
            'int[]': 'int*',
            'String': 'char*',
            'String[]': 'char**'
        }
        return type_map.get(type, type)
    
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
        var_name = ctx.Identifier()
        expression = self.visit(ctx.expression())
        self.emit(f"{var_name} = {expression};")

    def visitBlockStatement(self, ctx: DecafParser.StatementContext):
        self.emit("{")
        self.indentation += 1
        self.visit(ctx.block())
        self.indentation -= 1
        self.emit("}")
    
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
    
    
    def visitPrintStatement(self, ctx: DecafParser.StatementContext):
        expr = self.visit(ctx.expression())
        self.emit(f"printf(\"%d\\n\", {expr});")

    def visitExpressionStatement(self, ctx: DecafParser.StatementContext):
        expr = self.visit(ctx.expression(0))
        print("VISTI ")
        self.emit(f"{expr};")

    def visitWhileStatement(self, ctx: DecafParser.WhileStatementContext):
        self.logger.debug("Enter while statement")
        condition = self.visit(ctx.expression())
        if condition == None:
            self.logger.error(f"Invalid while condition at {ctx.start.line}")
            
        self.emit(f"while ({condition}) {{")
        self.indentation += 1
        self.visit(ctx.whileBlock())
        self.indentation -= 1
        self.emit("}")

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
        return f"{array}[{index}]"

    def visitArrayLengthExpression(self, ctx: DecafParser.ArrayLengthExpressionContext) -> str:
        self.logger.debug("Visiting array length expression")
        array = self.visit(ctx.expression())
        return f"sizeof({array})/sizeof({array}[0])"

    def visitMethodCallExpression(self, ctx: DecafParser.MethodCallExpressionContext) -> str:
        self.logger.debug("Visiting method call expression")
        obj = self.visit(ctx.expression(0))
        method = ctx.Identifier().getText()
        args = [obj]
        if len(ctx.expression()) > 1:
            args.extend([self.visit(expr) for expr in ctx.expression()[1:]])
        return f"{obj}->{method}({', '.join(args)})"

    def visitNotExpression(self, ctx: DecafParser.NotExpressionContext) -> str:
        self.logger.debug("Visiting NOT expression")
        expr = self.visit(ctx.expression())
        return f"!{expr}"

    def visitArrayInstantiationExpression(self, ctx: DecafParser.ArrayInstantiationExpressionContext) -> str:
        self.logger.debug("Visiting array instantiation expression")
        size = self.visit(ctx.expression())
        return f"(int*)malloc({size} * sizeof(int))"

    def visitObjectInstantiationExpression(self, ctx: DecafParser.ObjectInstantiationExpressionContext) -> str:
        self.logger.debug("Visiting object instantiation expression")
        class_name = ctx.Identifier().getText()
        return f"({class_name}*)malloc(sizeof({class_name}))"

    def visitPowExpression(self, ctx: DecafParser.PowExpressionContext) -> str:
        self.logger.debug("Visiting power expression")
        base = self.visit(ctx.expression(0))
        exp = self.visit(ctx.expression(1))
        return f"pow({base}, {exp})"

    def visitMulExpression(self, ctx: DecafParser.MulExpressionContext) -> str:
        self.logger.debug("Visiting multiplication expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return f"{left} * {right}"

    def visitAddExpression(self, ctx: DecafParser.AddExpressionContext) -> str:
        self.logger.debug("Visiting addition expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return f"{left} + {right}"

    def visitSubExpression(self, ctx: DecafParser.SubExpressionContext) -> str:
        self.logger.debug("Visiting subtraction expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
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

    def visitIdentifierExpression(self, ctx: DecafParser.IdentifierExpressionContext) -> str:
        self.logger.debug("Visiting identifier expression")
        return ctx.Identifier().getText()

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
        # Forward declare all classes as structs
        for class_decl in ctx.classDeclaration():
            class_name = class_decl.Identifier(0).getText()
            self.emit(f"typedef struct {class_name} {class_name};")
        self.emit("")
    
    def indent(self) -> str:
        return "    " * self.indentation
    
    def emit(self, code: str):
        self.output.append(self.indent() + code)