// Generated from /Users/amirali/Projects/Compiler/decaf/grammar/Decaf.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DecafLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, AND=21, LT=22, PLUS=23, MINUS=24, TIMES=25, 
		POWER=26, NOT=27, LSB=28, RSB=29, DOTLENGTH=30, LP=31, RP=32, RETURN=33, 
		EQ=34, EQL=35, BooleanLiteral=36, Identifier=37, IntegerLiteral=38, WS=39, 
		MULTILINE_COMMENT=40, LINE_COMMENT=41;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "T__19", "AND", "LT", "PLUS", "MINUS", "TIMES", "POWER", 
			"NOT", "LSB", "RSB", "DOTLENGTH", "LP", "RP", "RETURN", "EQ", "EQL", 
			"BooleanLiteral", "Identifier", "JavaLetter", "JavaLetterOrDigit", "IntegerLiteral", 
			"DecimalIntegerLiteral", "IntegertypeSuffix", "DecimalNumeral", "Digits", 
			"Digit", "NonZeroDigit", "DigitsAndUnderscores", "DigitOrUnderscore", 
			"Underscores", "WS", "MULTILINE_COMMENT", "LINE_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'{'", "'public'", "'static'", "'void'", "'main'", "'String'", 
			"'}'", "'extends'", "';'", "','", "'int'", "'boolean'", "'if'", "'else'", 
			"'while'", "'System.out.println'", "'.'", "'new'", "'this'", "'&&'", 
			"'<'", "'+'", "'-'", "'*'", "'**'", "'!'", "'['", "']'", "'.length'", 
			"'('", "')'", "'return'", "'='", "'=='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "AND", "LT", "PLUS", 
			"MINUS", "TIMES", "POWER", "NOT", "LSB", "RSB", "DOTLENGTH", "LP", "RP", 
			"RETURN", "EQ", "EQL", "BooleanLiteral", "Identifier", "IntegerLiteral", 
			"WS", "MULTILINE_COMMENT", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public DecafLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Decaf.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2+\u016b\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3"+
		"\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25"+
		"\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32"+
		"\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37"+
		"\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3"+
		"$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u010e\n%\3&\3&\7&\u0112\n&\f&\16&\u0115"+
		"\13&\3\'\3\'\3(\3(\3)\3)\3*\3*\5*\u011f\n*\3+\3+\3,\3,\3,\5,\u0126\n,"+
		"\3,\3,\3,\5,\u012b\n,\5,\u012d\n,\3-\3-\5-\u0131\n-\3-\5-\u0134\n-\3."+
		"\3.\5.\u0138\n.\3/\3/\3\60\6\60\u013d\n\60\r\60\16\60\u013e\3\61\3\61"+
		"\5\61\u0143\n\61\3\62\6\62\u0146\n\62\r\62\16\62\u0147\3\63\6\63\u014b"+
		"\n\63\r\63\16\63\u014c\3\63\3\63\3\64\3\64\3\64\3\64\7\64\u0155\n\64\f"+
		"\64\16\64\u0158\13\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\7\65"+
		"\u0163\n\65\f\65\16\65\u0166\13\65\3\65\3\65\3\65\3\65\4\u0156\u0164\2"+
		"\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36"+
		";\37= ?!A\"C#E$G%I&K\'M\2O\2Q(S\2U\2W\2Y\2[\2]\2_\2a\2c\2e)g*i+\3\2\7"+
		"\6\2&&C\\aac|\7\2&&\62;C\\aac|\4\2NNnn\3\2\63;\5\2\13\f\17\17\"\"\2\u016e"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3"+
		"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2"+
		"\2\2I\3\2\2\2\2K\3\2\2\2\2Q\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3"+
		"k\3\2\2\2\5q\3\2\2\2\7s\3\2\2\2\tz\3\2\2\2\13\u0081\3\2\2\2\r\u0086\3"+
		"\2\2\2\17\u008b\3\2\2\2\21\u0092\3\2\2\2\23\u0094\3\2\2\2\25\u009c\3\2"+
		"\2\2\27\u009e\3\2\2\2\31\u00a0\3\2\2\2\33\u00a4\3\2\2\2\35\u00ac\3\2\2"+
		"\2\37\u00af\3\2\2\2!\u00b4\3\2\2\2#\u00ba\3\2\2\2%\u00cd\3\2\2\2\'\u00cf"+
		"\3\2\2\2)\u00d3\3\2\2\2+\u00d8\3\2\2\2-\u00db\3\2\2\2/\u00dd\3\2\2\2\61"+
		"\u00df\3\2\2\2\63\u00e1\3\2\2\2\65\u00e3\3\2\2\2\67\u00e6\3\2\2\29\u00e8"+
		"\3\2\2\2;\u00ea\3\2\2\2=\u00ec\3\2\2\2?\u00f4\3\2\2\2A\u00f6\3\2\2\2C"+
		"\u00f8\3\2\2\2E\u00ff\3\2\2\2G\u0101\3\2\2\2I\u010d\3\2\2\2K\u010f\3\2"+
		"\2\2M\u0116\3\2\2\2O\u0118\3\2\2\2Q\u011a\3\2\2\2S\u011c\3\2\2\2U\u0120"+
		"\3\2\2\2W\u012c\3\2\2\2Y\u012e\3\2\2\2[\u0137\3\2\2\2]\u0139\3\2\2\2_"+
		"\u013c\3\2\2\2a\u0142\3\2\2\2c\u0145\3\2\2\2e\u014a\3\2\2\2g\u0150\3\2"+
		"\2\2i\u015e\3\2\2\2kl\7e\2\2lm\7n\2\2mn\7c\2\2no\7u\2\2op\7u\2\2p\4\3"+
		"\2\2\2qr\7}\2\2r\6\3\2\2\2st\7r\2\2tu\7w\2\2uv\7d\2\2vw\7n\2\2wx\7k\2"+
		"\2xy\7e\2\2y\b\3\2\2\2z{\7u\2\2{|\7v\2\2|}\7c\2\2}~\7v\2\2~\177\7k\2\2"+
		"\177\u0080\7e\2\2\u0080\n\3\2\2\2\u0081\u0082\7x\2\2\u0082\u0083\7q\2"+
		"\2\u0083\u0084\7k\2\2\u0084\u0085\7f\2\2\u0085\f\3\2\2\2\u0086\u0087\7"+
		"o\2\2\u0087\u0088\7c\2\2\u0088\u0089\7k\2\2\u0089\u008a\7p\2\2\u008a\16"+
		"\3\2\2\2\u008b\u008c\7U\2\2\u008c\u008d\7v\2\2\u008d\u008e\7t\2\2\u008e"+
		"\u008f\7k\2\2\u008f\u0090\7p\2\2\u0090\u0091\7i\2\2\u0091\20\3\2\2\2\u0092"+
		"\u0093\7\177\2\2\u0093\22\3\2\2\2\u0094\u0095\7g\2\2\u0095\u0096\7z\2"+
		"\2\u0096\u0097\7v\2\2\u0097\u0098\7g\2\2\u0098\u0099\7p\2\2\u0099\u009a"+
		"\7f\2\2\u009a\u009b\7u\2\2\u009b\24\3\2\2\2\u009c\u009d\7=\2\2\u009d\26"+
		"\3\2\2\2\u009e\u009f\7.\2\2\u009f\30\3\2\2\2\u00a0\u00a1\7k\2\2\u00a1"+
		"\u00a2\7p\2\2\u00a2\u00a3\7v\2\2\u00a3\32\3\2\2\2\u00a4\u00a5\7d\2\2\u00a5"+
		"\u00a6\7q\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7g\2\2"+
		"\u00a9\u00aa\7c\2\2\u00aa\u00ab\7p\2\2\u00ab\34\3\2\2\2\u00ac\u00ad\7"+
		"k\2\2\u00ad\u00ae\7h\2\2\u00ae\36\3\2\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1"+
		"\7n\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3\7g\2\2\u00b3 \3\2\2\2\u00b4\u00b5"+
		"\7y\2\2\u00b5\u00b6\7j\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7n\2\2\u00b8"+
		"\u00b9\7g\2\2\u00b9\"\3\2\2\2\u00ba\u00bb\7U\2\2\u00bb\u00bc\7{\2\2\u00bc"+
		"\u00bd\7u\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7o\2\2"+
		"\u00c0\u00c1\7\60\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4"+
		"\7v\2\2\u00c4\u00c5\7\60\2\2\u00c5\u00c6\7r\2\2\u00c6\u00c7\7t\2\2\u00c7"+
		"\u00c8\7k\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\7n\2\2"+
		"\u00cb\u00cc\7p\2\2\u00cc$\3\2\2\2\u00cd\u00ce\7\60\2\2\u00ce&\3\2\2\2"+
		"\u00cf\u00d0\7p\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7y\2\2\u00d2(\3\2\2"+
		"\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7j\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7"+
		"\7u\2\2\u00d7*\3\2\2\2\u00d8\u00d9\7(\2\2\u00d9\u00da\7(\2\2\u00da,\3"+
		"\2\2\2\u00db\u00dc\7>\2\2\u00dc.\3\2\2\2\u00dd\u00de\7-\2\2\u00de\60\3"+
		"\2\2\2\u00df\u00e0\7/\2\2\u00e0\62\3\2\2\2\u00e1\u00e2\7,\2\2\u00e2\64"+
		"\3\2\2\2\u00e3\u00e4\7,\2\2\u00e4\u00e5\7,\2\2\u00e5\66\3\2\2\2\u00e6"+
		"\u00e7\7#\2\2\u00e78\3\2\2\2\u00e8\u00e9\7]\2\2\u00e9:\3\2\2\2\u00ea\u00eb"+
		"\7_\2\2\u00eb<\3\2\2\2\u00ec\u00ed\7\60\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef"+
		"\7g\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7i\2\2\u00f1\u00f2\7v\2\2\u00f2"+
		"\u00f3\7j\2\2\u00f3>\3\2\2\2\u00f4\u00f5\7*\2\2\u00f5@\3\2\2\2\u00f6\u00f7"+
		"\7+\2\2\u00f7B\3\2\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb"+
		"\7v\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7p\2\2\u00fe"+
		"D\3\2\2\2\u00ff\u0100\7?\2\2\u0100F\3\2\2\2\u0101\u0102\7?\2\2\u0102\u0103"+
		"\7?\2\2\u0103H\3\2\2\2\u0104\u0105\7v\2\2\u0105\u0106\7t\2\2\u0106\u0107"+
		"\7w\2\2\u0107\u010e\7g\2\2\u0108\u0109\7h\2\2\u0109\u010a\7c\2\2\u010a"+
		"\u010b\7n\2\2\u010b\u010c\7u\2\2\u010c\u010e\7g\2\2\u010d\u0104\3\2\2"+
		"\2\u010d\u0108\3\2\2\2\u010eJ\3\2\2\2\u010f\u0113\5M\'\2\u0110\u0112\5"+
		"O(\2\u0111\u0110\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113"+
		"\u0114\3\2\2\2\u0114L\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0117\t\2\2\2"+
		"\u0117N\3\2\2\2\u0118\u0119\t\3\2\2\u0119P\3\2\2\2\u011a\u011b\5S*\2\u011b"+
		"R\3\2\2\2\u011c\u011e\5W,\2\u011d\u011f\5U+\2\u011e\u011d\3\2\2\2\u011e"+
		"\u011f\3\2\2\2\u011fT\3\2\2\2\u0120\u0121\t\4\2\2\u0121V\3\2\2\2\u0122"+
		"\u012d\7\62\2\2\u0123\u012a\5]/\2\u0124\u0126\5Y-\2\u0125\u0124\3\2\2"+
		"\2\u0125\u0126\3\2\2\2\u0126\u012b\3\2\2\2\u0127\u0128\5c\62\2\u0128\u0129"+
		"\5Y-\2\u0129\u012b\3\2\2\2\u012a\u0125\3\2\2\2\u012a\u0127\3\2\2\2\u012b"+
		"\u012d\3\2\2\2\u012c\u0122\3\2\2\2\u012c\u0123\3\2\2\2\u012dX\3\2\2\2"+
		"\u012e\u0133\5[.\2\u012f\u0131\5_\60\2\u0130\u012f\3\2\2\2\u0130\u0131"+
		"\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134\5[.\2\u0133\u0130\3\2\2\2\u0133"+
		"\u0134\3\2\2\2\u0134Z\3\2\2\2\u0135\u0138\7\62\2\2\u0136\u0138\5]/\2\u0137"+
		"\u0135\3\2\2\2\u0137\u0136\3\2\2\2\u0138\\\3\2\2\2\u0139\u013a\t\5\2\2"+
		"\u013a^\3\2\2\2\u013b\u013d\5a\61\2\u013c\u013b\3\2\2\2\u013d\u013e\3"+
		"\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f`\3\2\2\2\u0140\u0143"+
		"\5[.\2\u0141\u0143\7a\2\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u0143"+
		"b\3\2\2\2\u0144\u0146\7a\2\2\u0145\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147"+
		"\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148d\3\2\2\2\u0149\u014b\t\6\2\2"+
		"\u014a\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d"+
		"\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\b\63\2\2\u014ff\3\2\2\2\u0150"+
		"\u0151\7\61\2\2\u0151\u0152\7,\2\2\u0152\u0156\3\2\2\2\u0153\u0155\13"+
		"\2\2\2\u0154\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0157\3\2\2\2\u0156"+
		"\u0154\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\7,"+
		"\2\2\u015a\u015b\7\61\2\2\u015b\u015c\3\2\2\2\u015c\u015d\b\64\2\2\u015d"+
		"h\3\2\2\2\u015e\u015f\7\61\2\2\u015f\u0160\7\61\2\2\u0160\u0164\3\2\2"+
		"\2\u0161\u0163\13\2\2\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2\2\u0164"+
		"\u0165\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0164\3\2"+
		"\2\2\u0167\u0168\7\f\2\2\u0168\u0169\3\2\2\2\u0169\u016a\b\65\2\2\u016a"+
		"j\3\2\2\2\22\2\u010d\u0113\u011e\u0125\u012a\u012c\u0130\u0133\u0137\u013e"+
		"\u0142\u0147\u014c\u0156\u0164\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}