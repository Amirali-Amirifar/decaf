from antlr.Java8Parser import Java8Parser
from antlr.Java8ParserVisitor import Java8ParserVisitor


class MyVisitor(Java8ParserVisitor):
    def __init__(self):
        super().__init__()

    def visitAssignment(self, ctx:Java8Parser.AssignmentContext):
        lhs = ctx.leftHandSide().getText();
        rhs = ctx.expression().getText();
        op = ctx.assignmentOperator().getText();
        # print(lhs,op, rhs)

    def visitLocalVariableDeclaration(self, ctx:Java8Parser.LocalVariableDeclarationContext):
        # print(ctx.variableModifier())
        print(ctx.unannType().getText(), end = " ")
        print(ctx.variableDeclaratorList().getText())
