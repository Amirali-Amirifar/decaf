import logging

from grammar.DecafParser import DecafParser
from grammar.DecafVisitor import DecafVisitor

from .symtable import SymbolTable

class SymTableVisitor(DecafVisitor):
    def __init__(self):
        super().__init__()
        # Configure logger
        self.logger = logging.getLogger("SymTableVisitor")
        self.logger.setLevel(logging.DEBUG)
        
        # Remove any existing handlers to prevent duplicates
        self.logger.handlers = []
        
        # Create console handler with formatting
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # Prevent propagation to root logger
        self.logger.propagate = False
        
        self.symTable = SymbolTable()

    def visitMainClass(self, ctx:DecafParser.MainClassContext):
        class_name = ctx.Identifier(0).getText()
        self.logger.info(f"Visiting main class: {class_name}")
        
        # Declare the main class
        if not self.symTable.declare_class(name=class_name):
            self.logger.error(f"Class {class_name} already declared")
            return
                
        self.symTable.enter_scope(scope_name=class_name)
    
        # Declare main method in the class scope
        method_name = "main"
        args_name = ctx.Identifier(1).getText()
        if not self.symTable.declare_method(name=method_name, return_type="void", parameters=[{args_name: 'String[]'}]):
            self.logger.error(f"Failed to declare main method")
            return
    
        # Enter main method scope
        self.symTable.enter_scope(scope_name=method_name)
        
        # Declare the args parameter in the main method scope
        if not self.symTable.declare_variable(name=args_name, type_str='String[]'):
            self.logger.error(f"Failed to declare args parameter")
            return
    
        # Visit method body
        # Handle all statements in the main method        
        self.visit(ctx.statement())
    
        self.symTable.exit_scope()  # exit method scope
        self.symTable.exit_scope()  # exit class scope

    def visitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        method_name = ctx.Identifier().getText()
        return_type = self.visit(ctx.type_())
        self.logger.info(f"Visiting method declaration: {method_name} -> {return_type}")
        
        # Collect parameters first
        parameters = []
        if ctx.parameterList():
            for param in ctx.parameterList().parameter():
                param_type = self.visit(param.type_())
                param_name = param.Identifier().getText()
                parameters.append({param_name: param_type})
                self.logger.debug(f"Method parameter: {param_name}: {param_type}")
        
        # Declare method in the class scope
        if not self.symTable.declare_method(name=method_name, return_type=return_type, parameters=parameters):
            self.logger.error(f"Failed to declare method {method_name}")
            return
        
        # Always create a method scope, even if it will be empty
        self.symTable.enter_scope(scope_name=method_name)
        
        # Declare parameters in method scope if any
        for param in parameters:
            for param_name, param_type in param.items():
                if not self.symTable.declare_variable(name=param_name, type_str=param_type):
                    self.logger.error(f"Failed to declare parameter {param_name}")
        
        # Visit method body
        self.visitChildren(ctx)
        
        self.logger.debug(f"Exiting method scope: {method_name}")
        self.symTable.exit_scope()  # exit method scope

    def visitClassDeclaration(self, ctx:DecafParser.ClassDeclarationContext):
        class_name = ctx.Identifier(0).getText()
        parent_class = ctx.Identifier(1).getText() if ctx.Identifier(1) else None
        
        self.logger.info(f"Visiting class declaration: {class_name}")
        
        # Check for duplicate class declaration
        if self.symTable.lookup(class_name):
            self.logger.error(f"Error: Class {class_name} already declared")
            return
            
        # Check if parent class exists
        if parent_class and not self.symTable.lookup(parent_class):
            self.logger.error(f"Error: Parent class {parent_class} not found")
            return
    
        # If this is an inner class, it will be in the scope of its parent class
        current_scope = self.symTable.current_scope
        
        # Declare the class
        if not self.symTable.declare_class(name=class_name, parent_class=parent_class):
            return
            
        # Enter the class scope
        self.symTable.enter_scope(scope_name=class_name)
        
        # Visit all class members
        self.visitChildren(ctx)
        
        self.symTable.exit_scope()

    def visitNestedStatement(self, ctx:DecafParser.NestedStatementContext):
        self.logger.debug("Entering nested block scope")
        self.symTable.enter_scope(scope_name="Block")
        for stmt in ctx.statement():
            self.visit(stmt)
        self.logger.debug("Exiting nested block scope")
        self.symTable.exit_scope()

    def visitIfElseStatement(self, ctx:DecafParser.IfElseStatementContext):
        self.logger.debug("Visiting if-else statement")
        condition_type = self.visit(ctx.expression())
        if condition_type != 'boolean':
            self.logger.error(f"Type error: If condition must be boolean, got {condition_type}")

        self.logger.debug("Entering if block scope")
        self.symTable.enter_scope(scope_name="IfBlock")
        self.visit(ctx.ifBlock())
        self.symTable.exit_scope()

        self.logger.debug("Entering else block scope")
        self.symTable.enter_scope(scope_name="ElseBlock")
        self.visit(ctx.elseBlock())
        self.symTable.exit_scope()

    def visitWhileStatement(self, ctx:DecafParser.WhileStatementContext):
        self.logger.debug("Visiting while statement")
        condition_type = self.visit(ctx.expression())
        if condition_type != 'boolean':
            self.logger.error(f"Type error: While condition must be boolean, got {condition_type}")

        self.logger.debug("Entering while block scope")
        self.symTable.enter_scope(scope_name="WhileBlock")
        self.visit(ctx.whileBlock())
        self.symTable.exit_scope()

    def visitPrintStatement(self, ctx:DecafParser.PrintStatementContext):
        self.logger.debug("Visiting print statement")
        expr_type = self.visit(ctx.expression())
        if expr_type not in ['int', 'boolean']:
            self.logger.error(f"Type error: Can only print int or boolean, got {expr_type}")

    def visitVariableAssignmentStatement(self, ctx:DecafParser.VariableAssignmentStatementContext):
        var_name = ctx.Identifier().getText()
        self.logger.debug(f"Visiting variable assignment: {var_name}")
        var_symbol = self.symTable.lookup(var_name)
        if not var_symbol:
            self.logger.error(f"Reference error: Variable {var_name} not declared")
            return

        expr_type = self.visit(ctx.expression())
        if var_symbol.type != expr_type:
            self.logger.error(f"Type error: Cannot assign {expr_type} to variable of type {var_symbol.type}")

    def visitArrayAssignmentStatement(self, ctx:DecafParser.ArrayAssignmentStatementContext):
        array_name = ctx.Identifier().getText()
        self.logger.debug(f"Visiting array assignment: {array_name}")
        array_symbol = self.symTable.lookup(array_name)
        if not array_symbol:
            self.logger.error(f"Reference error: Array {array_name} not declared")
            return

        if array_symbol.type != 'int[]':
            self.logger.error(f"Type error: Variable {array_name} is not an array")
            return

        index_type = self.visit(ctx.expression(0))
        if index_type != 'int':
            self.logger.error(f"Type error: Array index must be int, got {index_type}")

        value_type = self.visit(ctx.expression(1))
        if value_type != 'int':
            self.logger.error(f"Type error: Array element must be int, got {value_type}")

    def visitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        method_name = ctx.Identifier().getText()
        return_type = self.visit(ctx.type_())
        self.logger.info(f"Visiting method declaration: {method_name} -> {return_type}")
        
        # Collect parameters first
        parameters = []
        if ctx.parameterList():
            for param in ctx.parameterList().parameter():
                param_type = self.visit(param.type_())
                param_name = param.Identifier().getText()
                parameters.append({param_name: param_type})
                self.logger.debug(f"Method parameter: {param_name}: {param_type}")
        
        # Declare method in the current scope
        if not self.symTable.declare_method(name=method_name, return_type=return_type, parameters=parameters):
            self.logger.error(f"Failed to declare method {method_name}")
            return
        
        # Enter method scope after declaring it
        self.symTable.enter_scope(scope_name=method_name)
        
        # Declare parameters in the method scope
        for param in parameters:
            for param_name, param_type in param.items():
                if not self.symTable.declare_variable(name=param_name, type_str=param_type):
                    self.logger.error(f"Failed to declare parameter {param_name}")
        
        # Visit method body
        self.visitChildren(ctx)
        
        self.logger.debug(f"Exiting method scope: {method_name}")
        self.symTable.exit_scope()

    def visitVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        var_type = self.visit(ctx.type_())
        var_name = ctx.Identifier().getText()
        self.logger.debug(f"Declaring variable: {var_name}: {var_type}")
        if not self.symTable.declare_variable(name=var_name, type_str=var_type):
            self.logger.error(f"Failed to declare variable {var_name} of type {var_type}")
            return

    def visitType(self, ctx:DecafParser.TypeContext):
        type_str = ctx.getText()
        self.logger.debug(f"Processing type: {type_str}")
        return type_str if type_str == 'int[]' else type_str

    def visitMethodBody(self, ctx:DecafParser.MethodBodyContext):
        self.logger.debug("Visiting method body")
        for local_decl in ctx.localDeclaration():
            self.visit(local_decl)
        
        for statement in ctx.statement():
            self.visit(statement)
        
        return_type = self.visit(ctx.expression())
        self.logger.debug(f"Method return type: {return_type}")
        return return_type

    def visitArrayAccessExpression(self, ctx:DecafParser.ArrayAccessExpressionContext):
        self.logger.debug("Visiting array access expression")
        array_expr = self.visit(ctx.expression(0))
        index_expr = self.visit(ctx.expression(1))
        if array_expr != 'int[]':
            self.logger.error(f"Type error: Cannot access index of non-array type {array_expr}")
        if index_expr != 'int':
            self.logger.error(f"Type error: Array index must be int, got {index_expr}")
        return 'int'

    def visitArrayLengthExpression(self, ctx:DecafParser.ArrayLengthExpressionContext):
        self.logger.debug("Visiting array length expression")
        array_expr = self.visit(ctx.expression())
        if array_expr != 'int[]':
            self.logger.error(f"Type error: Cannot get length of non-array type {array_expr}")
        return 'int'

    def visitMethodCallExpression(self, ctx:DecafParser.MethodCallExpressionContext):
        obj_expr = self.visit(ctx.expression(0))
        method_name = ctx.Identifier().getText()
        self.logger.debug(f"Visiting method call: {method_name} on object of type {obj_expr}")
        args = [self.visit(expr) for expr in ctx.expression()[1:]]
        self.logger.debug(f"Method call arguments types: {args}")
        return obj_expr

    def visitNotExpression(self, ctx:DecafParser.NotExpressionContext):
        self.logger.debug("Visiting not expression")
        expr = self.visit(ctx.expression())
        if expr != 'boolean':
            self.logger.error(f"Type error: Cannot apply 'not' to non-boolean type {expr}")
        return 'boolean'

    def visitArrayInstantiationExpression(self, ctx:DecafParser.ArrayInstantiationExpressionContext):
        self.logger.debug("Visiting array instantiation")
        size_expr = self.visit(ctx.expression())
        if size_expr != 'int':
            self.logger.error(f"Type error: Array size must be int, got {size_expr}")
        return 'int[]'

    def visitObjectInstantiationExpression(self, ctx:DecafParser.ObjectInstantiationExpressionContext):
        class_name = ctx.Identifier().getText()
        self.logger.debug(f"Visiting object instantiation: {class_name}")
        return class_name

    def visitPowExpression(self, ctx:DecafParser.PowExpressionContext):
        self.logger.debug("Visiting power expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != 'int' or right != 'int':
            self.logger.error(f"Type error: Power operation requires int operands, got {left} and {right}")
        return 'int'

    def visitMulExpression(self, ctx:DecafParser.MulExpressionContext):
        self.logger.debug("Visiting multiplication expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != 'int' or right != 'int':
            self.logger.error(f"Type error: Multiplication requires int operands, got {left} and {right}")
        return 'int'

    def visitAddExpression(self, ctx:DecafParser.AddExpressionContext):
        self.logger.debug("Visiting addition expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != 'int' or right != 'int':
            self.logger.error(f"Type error: Addition requires int operands, got {left} and {right}")
        return 'int'

    def visitSubExpression(self, ctx:DecafParser.SubExpressionContext):
        self.logger.debug("Visiting subtraction expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != 'int' or right != 'int':
            self.logger.error(f"Type error: Subtraction requires int operands, got {left} and {right}")
        return 'int'

    def visitLtExpression(self, ctx:DecafParser.LtExpressionContext):
        self.logger.debug("Visiting less than expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != 'int' or right != 'int':
            self.logger.error(f"Type error: Less than comparison requires int operands, got {left} and {right}")
        return 'boolean'

    def visitAndExpression(self, ctx:DecafParser.AndExpressionContext):
        self.logger.debug("Visiting and expression")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != 'boolean' or right != 'boolean':
            self.logger.error(f"Type error: AND operation requires boolean operands, got {left} and {right}")
        return 'boolean'

    def visitIntLitExpression(self, ctx:DecafParser.IntLitExpressionContext):
        self.logger.debug("Visiting integer literal")
        return 'int'

    def visitBooleanLitExpression(self, ctx:DecafParser.BooleanLitExpressionContext):
        self.logger.debug("Visiting boolean literal")
        return 'boolean'

    def visitIdentifierExpression(self, ctx:DecafParser.IdentifierExpressionContext):
        var_name = ctx.Identifier().getText()
        self.logger.debug(f"Visiting identifier")
        symbol = self.symTable.lookup(var_name)
        if symbol:
            return symbol.type
        return None

    def visitThisExpression(self, ctx:DecafParser.ThisExpressionContext):
        # Get the current class scope
        current_scope = self.symTable.current_scope
        class_name = current_scope.split('.')[1] if '.' in current_scope else current_scope
        return class_name

    def visitParenExpression(self, ctx:DecafParser.ParenExpressionContext):
        return self.visit(ctx.expression())