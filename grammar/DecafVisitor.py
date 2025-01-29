# Generated from Decaf.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete generic visitor for a parse tree produced by DecafParser.

class DecafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DecafParser#goal.
    def visitGoal(self, ctx:DecafParser.GoalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#mainClass.
    def visitMainClass(self, ctx:DecafParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#classDeclaration.
    def visitClassDeclaration(self, ctx:DecafParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:DecafParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#localDeclaration.
    def visitLocalDeclaration(self, ctx:DecafParser.LocalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#varDeclaration.
    def visitVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#parameterList.
    def visitParameterList(self, ctx:DecafParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#parameter.
    def visitParameter(self, ctx:DecafParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#methodBody.
    def visitMethodBody(self, ctx:DecafParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#type.
    def visitType(self, ctx:DecafParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#nestedStatement.
    def visitNestedStatement(self, ctx:DecafParser.NestedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#ifElseStatement.
    def visitIfElseStatement(self, ctx:DecafParser.IfElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#whileStatement.
    def visitWhileStatement(self, ctx:DecafParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#printStatement.
    def visitPrintStatement(self, ctx:DecafParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#variableAssignmentStatement.
    def visitVariableAssignmentStatement(self, ctx:DecafParser.VariableAssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arrayAssignmentStatement.
    def visitArrayAssignmentStatement(self, ctx:DecafParser.ArrayAssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#ifBlock.
    def visitIfBlock(self, ctx:DecafParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#elseBlock.
    def visitElseBlock(self, ctx:DecafParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#whileBlock.
    def visitWhileBlock(self, ctx:DecafParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#ltExpression.
    def visitLtExpression(self, ctx:DecafParser.LtExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#objectInstantiationExpression.
    def visitObjectInstantiationExpression(self, ctx:DecafParser.ObjectInstantiationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arrayInstantiationExpression.
    def visitArrayInstantiationExpression(self, ctx:DecafParser.ArrayInstantiationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#powExpression.
    def visitPowExpression(self, ctx:DecafParser.PowExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:DecafParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#methodCallExpression.
    def visitMethodCallExpression(self, ctx:DecafParser.MethodCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#notExpression.
    def visitNotExpression(self, ctx:DecafParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#booleanLitExpression.
    def visitBooleanLitExpression(self, ctx:DecafParser.BooleanLitExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#parenExpression.
    def visitParenExpression(self, ctx:DecafParser.ParenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#intLitExpression.
    def visitIntLitExpression(self, ctx:DecafParser.IntLitExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#eqExpression.
    def visitEqExpression(self, ctx:DecafParser.EqExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#andExpression.
    def visitAndExpression(self, ctx:DecafParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arrayAccessExpression.
    def visitArrayAccessExpression(self, ctx:DecafParser.ArrayAccessExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#addExpression.
    def visitAddExpression(self, ctx:DecafParser.AddExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#thisExpression.
    def visitThisExpression(self, ctx:DecafParser.ThisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arrayLengthExpression.
    def visitArrayLengthExpression(self, ctx:DecafParser.ArrayLengthExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#subExpression.
    def visitSubExpression(self, ctx:DecafParser.SubExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#mulExpression.
    def visitMulExpression(self, ctx:DecafParser.MulExpressionContext):
        return self.visitChildren(ctx)



del DecafParser