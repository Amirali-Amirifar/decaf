// Generated from /Users/amirali/Projects/Compiler/decaf/grammar/Decaf.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DecafParser}.
 */
public interface DecafListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DecafParser#goal}.
	 * @param ctx the parse tree
	 */
	void enterGoal(DecafParser.GoalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#goal}.
	 * @param ctx the parse tree
	 */
	void exitGoal(DecafParser.GoalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#mainClass}.
	 * @param ctx the parse tree
	 */
	void enterMainClass(DecafParser.MainClassContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#mainClass}.
	 * @param ctx the parse tree
	 */
	void exitMainClass(DecafParser.MainClassContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#classDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterClassDeclaration(DecafParser.ClassDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#classDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitClassDeclaration(DecafParser.ClassDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#fieldDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterFieldDeclaration(DecafParser.FieldDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#fieldDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitFieldDeclaration(DecafParser.FieldDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#localDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterLocalDeclaration(DecafParser.LocalDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#localDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitLocalDeclaration(DecafParser.LocalDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclaration(DecafParser.VarDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclaration(DecafParser.VarDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterMethodDeclaration(DecafParser.MethodDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitMethodDeclaration(DecafParser.MethodDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void enterParameterList(DecafParser.ParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void exitParameterList(DecafParser.ParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(DecafParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(DecafParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#methodBody}.
	 * @param ctx the parse tree
	 */
	void enterMethodBody(DecafParser.MethodBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#methodBody}.
	 * @param ctx the parse tree
	 */
	void exitMethodBody(DecafParser.MethodBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(DecafParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(DecafParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nestedStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterNestedStatement(DecafParser.NestedStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nestedStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitNestedStatement(DecafParser.NestedStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifElseStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfElseStatement(DecafParser.IfElseStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifElseStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfElseStatement(DecafParser.IfElseStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(DecafParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(DecafParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterPrintStatement(DecafParser.PrintStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitPrintStatement(DecafParser.PrintStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code variableAssignmentStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterVariableAssignmentStatement(DecafParser.VariableAssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code variableAssignmentStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitVariableAssignmentStatement(DecafParser.VariableAssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arrayAssignmentStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterArrayAssignmentStatement(DecafParser.ArrayAssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arrayAssignmentStatement}
	 * labeled alternative in {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitArrayAssignmentStatement(DecafParser.ArrayAssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void enterIfBlock(DecafParser.IfBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void exitIfBlock(DecafParser.IfBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#elseBlock}.
	 * @param ctx the parse tree
	 */
	void enterElseBlock(DecafParser.ElseBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#elseBlock}.
	 * @param ctx the parse tree
	 */
	void exitElseBlock(DecafParser.ElseBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#whileBlock}.
	 * @param ctx the parse tree
	 */
	void enterWhileBlock(DecafParser.WhileBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#whileBlock}.
	 * @param ctx the parse tree
	 */
	void exitWhileBlock(DecafParser.WhileBlockContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ltExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLtExpression(DecafParser.LtExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ltExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLtExpression(DecafParser.LtExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code objectInstantiationExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterObjectInstantiationExpression(DecafParser.ObjectInstantiationExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code objectInstantiationExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitObjectInstantiationExpression(DecafParser.ObjectInstantiationExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arrayInstantiationExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterArrayInstantiationExpression(DecafParser.ArrayInstantiationExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arrayInstantiationExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitArrayInstantiationExpression(DecafParser.ArrayInstantiationExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code powExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterPowExpression(DecafParser.PowExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code powExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitPowExpression(DecafParser.PowExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code identifierExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierExpression(DecafParser.IdentifierExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code identifierExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierExpression(DecafParser.IdentifierExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code methodCallExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMethodCallExpression(DecafParser.MethodCallExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code methodCallExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMethodCallExpression(DecafParser.MethodCallExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code notExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNotExpression(DecafParser.NotExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code notExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNotExpression(DecafParser.NotExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code booleanLitExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLitExpression(DecafParser.BooleanLitExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code booleanLitExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLitExpression(DecafParser.BooleanLitExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterParenExpression(DecafParser.ParenExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitParenExpression(DecafParser.ParenExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intLitExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIntLitExpression(DecafParser.IntLitExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intLitExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIntLitExpression(DecafParser.IntLitExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code andExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAndExpression(DecafParser.AndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code andExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAndExpression(DecafParser.AndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arrayAccessExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterArrayAccessExpression(DecafParser.ArrayAccessExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arrayAccessExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitArrayAccessExpression(DecafParser.ArrayAccessExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code addExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAddExpression(DecafParser.AddExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code addExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAddExpression(DecafParser.AddExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code thisExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterThisExpression(DecafParser.ThisExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code thisExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitThisExpression(DecafParser.ThisExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arrayLengthExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterArrayLengthExpression(DecafParser.ArrayLengthExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arrayLengthExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitArrayLengthExpression(DecafParser.ArrayLengthExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code subExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterSubExpression(DecafParser.SubExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code subExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitSubExpression(DecafParser.SubExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mulExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMulExpression(DecafParser.MulExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mulExpression}
	 * labeled alternative in {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMulExpression(DecafParser.MulExpressionContext ctx);
}