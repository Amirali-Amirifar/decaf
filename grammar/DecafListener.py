# Generated from Decaf.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete listener for a parse tree produced by DecafParser.
class DecafListener(ParseTreeListener):

    # Enter a parse tree produced by DecafParser#goal.
    def enterGoal(self, ctx:DecafParser.GoalContext):
        pass

    # Exit a parse tree produced by DecafParser#goal.
    def exitGoal(self, ctx:DecafParser.GoalContext):
        pass


    # Enter a parse tree produced by DecafParser#mainClass.
    def enterMainClass(self, ctx:DecafParser.MainClassContext):
        pass

    # Exit a parse tree produced by DecafParser#mainClass.
    def exitMainClass(self, ctx:DecafParser.MainClassContext):
        pass


    # Enter a parse tree produced by DecafParser#classDeclaration.
    def enterClassDeclaration(self, ctx:DecafParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#classDeclaration.
    def exitClassDeclaration(self, ctx:DecafParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:DecafParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:DecafParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#localDeclaration.
    def enterLocalDeclaration(self, ctx:DecafParser.LocalDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#localDeclaration.
    def exitLocalDeclaration(self, ctx:DecafParser.LocalDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#varDeclaration.
    def enterVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#varDeclaration.
    def exitVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#parameterList.
    def enterParameterList(self, ctx:DecafParser.ParameterListContext):
        pass

    # Exit a parse tree produced by DecafParser#parameterList.
    def exitParameterList(self, ctx:DecafParser.ParameterListContext):
        pass


    # Enter a parse tree produced by DecafParser#parameter.
    def enterParameter(self, ctx:DecafParser.ParameterContext):
        pass

    # Exit a parse tree produced by DecafParser#parameter.
    def exitParameter(self, ctx:DecafParser.ParameterContext):
        pass


    # Enter a parse tree produced by DecafParser#methodBody.
    def enterMethodBody(self, ctx:DecafParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by DecafParser#methodBody.
    def exitMethodBody(self, ctx:DecafParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by DecafParser#type.
    def enterType(self, ctx:DecafParser.TypeContext):
        pass

    # Exit a parse tree produced by DecafParser#type.
    def exitType(self, ctx:DecafParser.TypeContext):
        pass


    # Enter a parse tree produced by DecafParser#nestedStatement.
    def enterNestedStatement(self, ctx:DecafParser.NestedStatementContext):
        pass

    # Exit a parse tree produced by DecafParser#nestedStatement.
    def exitNestedStatement(self, ctx:DecafParser.NestedStatementContext):
        pass


    # Enter a parse tree produced by DecafParser#ifElseStatement.
    def enterIfElseStatement(self, ctx:DecafParser.IfElseStatementContext):
        pass

    # Exit a parse tree produced by DecafParser#ifElseStatement.
    def exitIfElseStatement(self, ctx:DecafParser.IfElseStatementContext):
        pass


    # Enter a parse tree produced by DecafParser#whileStatement.
    def enterWhileStatement(self, ctx:DecafParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by DecafParser#whileStatement.
    def exitWhileStatement(self, ctx:DecafParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by DecafParser#printStatement.
    def enterPrintStatement(self, ctx:DecafParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by DecafParser#printStatement.
    def exitPrintStatement(self, ctx:DecafParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by DecafParser#variableAssignmentStatement.
    def enterVariableAssignmentStatement(self, ctx:DecafParser.VariableAssignmentStatementContext):
        pass

    # Exit a parse tree produced by DecafParser#variableAssignmentStatement.
    def exitVariableAssignmentStatement(self, ctx:DecafParser.VariableAssignmentStatementContext):
        pass


    # Enter a parse tree produced by DecafParser#arrayAssignmentStatement.
    def enterArrayAssignmentStatement(self, ctx:DecafParser.ArrayAssignmentStatementContext):
        pass

    # Exit a parse tree produced by DecafParser#arrayAssignmentStatement.
    def exitArrayAssignmentStatement(self, ctx:DecafParser.ArrayAssignmentStatementContext):
        pass


    # Enter a parse tree produced by DecafParser#ifBlock.
    def enterIfBlock(self, ctx:DecafParser.IfBlockContext):
        pass

    # Exit a parse tree produced by DecafParser#ifBlock.
    def exitIfBlock(self, ctx:DecafParser.IfBlockContext):
        pass


    # Enter a parse tree produced by DecafParser#elseBlock.
    def enterElseBlock(self, ctx:DecafParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by DecafParser#elseBlock.
    def exitElseBlock(self, ctx:DecafParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by DecafParser#whileBlock.
    def enterWhileBlock(self, ctx:DecafParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by DecafParser#whileBlock.
    def exitWhileBlock(self, ctx:DecafParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by DecafParser#ltExpression.
    def enterLtExpression(self, ctx:DecafParser.LtExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#ltExpression.
    def exitLtExpression(self, ctx:DecafParser.LtExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#objectInstantiationExpression.
    def enterObjectInstantiationExpression(self, ctx:DecafParser.ObjectInstantiationExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#objectInstantiationExpression.
    def exitObjectInstantiationExpression(self, ctx:DecafParser.ObjectInstantiationExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#arrayInstantiationExpression.
    def enterArrayInstantiationExpression(self, ctx:DecafParser.ArrayInstantiationExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#arrayInstantiationExpression.
    def exitArrayInstantiationExpression(self, ctx:DecafParser.ArrayInstantiationExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#powExpression.
    def enterPowExpression(self, ctx:DecafParser.PowExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#powExpression.
    def exitPowExpression(self, ctx:DecafParser.PowExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:DecafParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:DecafParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#methodCallExpression.
    def enterMethodCallExpression(self, ctx:DecafParser.MethodCallExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#methodCallExpression.
    def exitMethodCallExpression(self, ctx:DecafParser.MethodCallExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#notExpression.
    def enterNotExpression(self, ctx:DecafParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#notExpression.
    def exitNotExpression(self, ctx:DecafParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#booleanLitExpression.
    def enterBooleanLitExpression(self, ctx:DecafParser.BooleanLitExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#booleanLitExpression.
    def exitBooleanLitExpression(self, ctx:DecafParser.BooleanLitExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#parenExpression.
    def enterParenExpression(self, ctx:DecafParser.ParenExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#parenExpression.
    def exitParenExpression(self, ctx:DecafParser.ParenExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#intLitExpression.
    def enterIntLitExpression(self, ctx:DecafParser.IntLitExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#intLitExpression.
    def exitIntLitExpression(self, ctx:DecafParser.IntLitExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#eqExpression.
    def enterEqExpression(self, ctx:DecafParser.EqExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#eqExpression.
    def exitEqExpression(self, ctx:DecafParser.EqExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#andExpression.
    def enterAndExpression(self, ctx:DecafParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#andExpression.
    def exitAndExpression(self, ctx:DecafParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#arrayAccessExpression.
    def enterArrayAccessExpression(self, ctx:DecafParser.ArrayAccessExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#arrayAccessExpression.
    def exitArrayAccessExpression(self, ctx:DecafParser.ArrayAccessExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#addExpression.
    def enterAddExpression(self, ctx:DecafParser.AddExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#addExpression.
    def exitAddExpression(self, ctx:DecafParser.AddExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#thisExpression.
    def enterThisExpression(self, ctx:DecafParser.ThisExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#thisExpression.
    def exitThisExpression(self, ctx:DecafParser.ThisExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#arrayLengthExpression.
    def enterArrayLengthExpression(self, ctx:DecafParser.ArrayLengthExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#arrayLengthExpression.
    def exitArrayLengthExpression(self, ctx:DecafParser.ArrayLengthExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#subExpression.
    def enterSubExpression(self, ctx:DecafParser.SubExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#subExpression.
    def exitSubExpression(self, ctx:DecafParser.SubExpressionContext):
        pass


    # Enter a parse tree produced by DecafParser#mulExpression.
    def enterMulExpression(self, ctx:DecafParser.MulExpressionContext):
        pass

    # Exit a parse tree produced by DecafParser#mulExpression.
    def exitMulExpression(self, ctx:DecafParser.MulExpressionContext):
        pass



del DecafParser