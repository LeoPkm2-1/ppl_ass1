# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u01a2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\7\2X\n\2\f\2")
        buf.write("\16\2[\13\2\3\2\3\2\6\2_\n\2\r\2\16\2`\7\2c\n\2\f\2\16")
        buf.write("\2f\13\2\3\2\3\2\5\2j\n\2\3\3\3\3\3\3\3\3\5\3p\n\3\3\3")
        buf.write("\3\3\7\3t\n\3\f\3\16\3w\13\3\3\3\3\3\6\3{\n\3\r\3\16\3")
        buf.write("|\7\3\177\n\3\f\3\16\3\u0082\13\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\u008b\n\3\5\3\u008d\n\3\3\4\3\4\3\4\7\4\u0092")
        buf.write("\n\4\f\4\16\4\u0095\13\4\3\4\3\4\6\4\u0099\n\4\r\4\16")
        buf.write("\4\u009a\7\4\u009d\n\4\f\4\16\4\u00a0\13\4\3\4\3\4\3\4")
        buf.write("\5\4\u00a5\n\4\3\5\3\5\3\5\3\5\5\5\u00ab\n\5\3\5\3\5\7")
        buf.write("\5\u00af\n\5\f\5\16\5\u00b2\13\5\3\5\3\5\6\5\u00b6\n\5")
        buf.write("\r\5\16\5\u00b7\7\5\u00ba\n\5\f\5\16\5\u00bd\13\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00c6\n\5\5\5\u00c8\n\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00e2\n\n")
        buf.write("\3\13\3\13\7\13\u00e6\n\13\f\13\16\13\u00e9\13\13\3\13")
        buf.write("\3\13\6\13\u00ed\n\13\r\13\16\13\u00ee\7\13\u00f1\n\13")
        buf.write("\f\13\16\13\u00f4\13\13\3\13\5\13\u00f7\n\13\3\f\3\f\7")
        buf.write("\f\u00fb\n\f\f\f\16\f\u00fe\13\f\3\r\3\r\5\r\u0102\n\r")
        buf.write("\3\r\6\r\u0105\n\r\r\r\16\r\u0106\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u0112\n\16\3\17\3\17\7")
        buf.write("\17\u0116\n\17\f\17\16\17\u0119\13\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\5\20\u0121\n\20\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\5\23\u012c\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\6#\u016a\n#\r#")
        buf.write("\16#\u016b\3#\7#\u016f\n#\f#\16#\u0172\13#\3$\3$\3%\3")
        buf.write("%\6%\u0178\n%\r%\16%\u0179\3%\7%\u017d\n%\f%\16%\u0180")
        buf.write("\13%\3&\6&\u0183\n&\r&\16&\u0184\3&\3&\3\'\3\'\7\'\u018b")
        buf.write("\n\'\f\'\16\'\u018e\13\'\3\'\3\'\3\'\3(\5(\u0194\n(\3")
        buf.write(")\3)\7)\u0198\n)\f)\16)\u019b\13)\3)\3)\3)\3*\3*\3*\2")
        buf.write("\2+\3\3\5\4\7\5\t\6\13\2\r\2\17\2\21\2\23\7\25\2\27\2")
        buf.write("\31\2\33\b\35\t\37\2!\2#\2%\2\'\n)\13+\f-\r/\16\61\17")
        buf.write("\63\20\65\21\67\229\23;\24=\25?\26A\27C\30E\31G\2I\32")
        buf.write("K\33M\34O\2Q\35S\36\3\2\22\3\2\63;\4\2\63;CH\3\2\639\3")
        buf.write("\2\62;\4\2\62;CH\3\2\629\3\2\62\63\4\2GGgg\4\2--//\7\2")
        buf.write("\n\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2^^\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\5\2\13\f\17\17\"\"\7\3\n\f\16\17$$))^^\2")
        buf.write("\u01be\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\3i\3\2\2\2\5\u008c\3\2\2\2\7\u00a4\3\2\2")
        buf.write("\2\t\u00c7\3\2\2\2\13\u00c9\3\2\2\2\r\u00cb\3\2\2\2\17")
        buf.write("\u00cd\3\2\2\2\21\u00cf\3\2\2\2\23\u00e1\3\2\2\2\25\u00f6")
        buf.write("\3\2\2\2\27\u00f8\3\2\2\2\31\u00ff\3\2\2\2\33\u0111\3")
        buf.write("\2\2\2\35\u0113\3\2\2\2\37\u0120\3\2\2\2!\u0122\3\2\2")
        buf.write("\2#\u0125\3\2\2\2%\u012b\3\2\2\2\'\u012d\3\2\2\2)\u0133")
        buf.write("\3\2\2\2+\u0139\3\2\2\2-\u013d\3\2\2\2/\u0141\3\2\2\2")
        buf.write("\61\u0143\3\2\2\2\63\u0145\3\2\2\2\65\u0147\3\2\2\2\67")
        buf.write("\u0149\3\2\2\29\u014b\3\2\2\2;\u014d\3\2\2\2=\u014f\3")
        buf.write("\2\2\2?\u0157\3\2\2\2A\u015b\3\2\2\2C\u0161\3\2\2\2E\u0169")
        buf.write("\3\2\2\2G\u0173\3\2\2\2I\u0175\3\2\2\2K\u0182\3\2\2\2")
        buf.write("M\u0188\3\2\2\2O\u0193\3\2\2\2Q\u0195\3\2\2\2S\u019f\3")
        buf.write("\2\2\2UY\t\2\2\2VX\5\13\6\2WV\3\2\2\2X[\3\2\2\2YW\3\2")
        buf.write("\2\2YZ\3\2\2\2Zd\3\2\2\2[Y\3\2\2\2\\^\7a\2\2]_\5\13\6")
        buf.write("\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2b")
        buf.write("\\\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2eg\3\2\2\2fd\3")
        buf.write("\2\2\2gj\b\2\2\2hj\7\62\2\2iU\3\2\2\2ih\3\2\2\2j\4\3\2")
        buf.write("\2\2kl\7\62\2\2lp\7z\2\2mn\7\62\2\2np\7Z\2\2ok\3\2\2\2")
        buf.write("om\3\2\2\2pq\3\2\2\2qu\t\3\2\2rt\5\r\7\2sr\3\2\2\2tw\3")
        buf.write("\2\2\2us\3\2\2\2uv\3\2\2\2v\u0080\3\2\2\2wu\3\2\2\2xz")
        buf.write("\7a\2\2y{\5\r\7\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2")
        buf.write("\2\2}\177\3\2\2\2~x\3\2\2\2\177\u0082\3\2\2\2\u0080~\3")
        buf.write("\2\2\2\u0080\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0083\u008d\b\3\3\2\u0084\u0085\7\62\2\2\u0085")
        buf.write("\u0086\7z\2\2\u0086\u008b\7\62\2\2\u0087\u0088\7\62\2")
        buf.write("\2\u0088\u0089\7Z\2\2\u0089\u008b\7\62\2\2\u008a\u0084")
        buf.write("\3\2\2\2\u008a\u0087\3\2\2\2\u008b\u008d\3\2\2\2\u008c")
        buf.write("o\3\2\2\2\u008c\u008a\3\2\2\2\u008d\6\3\2\2\2\u008e\u008f")
        buf.write("\7\62\2\2\u008f\u0093\t\4\2\2\u0090\u0092\5\17\b\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0093\u0094\3\2\2\2\u0094\u009e\3\2\2\2\u0095\u0093\3")
        buf.write("\2\2\2\u0096\u0098\7a\2\2\u0097\u0099\5\17\b\2\u0098\u0097")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u0096\3\2\2\2")
        buf.write("\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3")
        buf.write("\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a5")
        buf.write("\b\4\4\2\u00a2\u00a3\7\62\2\2\u00a3\u00a5\7\62\2\2\u00a4")
        buf.write("\u008e\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\b\3\2\2\2\u00a6")
        buf.write("\u00a7\7\62\2\2\u00a7\u00ab\7d\2\2\u00a8\u00a9\7\62\2")
        buf.write("\2\u00a9\u00ab\7D\2\2\u00aa\u00a6\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00b0\7\63\2\2\u00ad")
        buf.write("\u00af\5\21\t\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2")
        buf.write("\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00bb")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\7a\2\2\u00b4")
        buf.write("\u00b6\5\21\t\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2")
        buf.write("\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba")
        buf.write("\3\2\2\2\u00b9\u00b3\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00be\u00c8\b\5\5\2\u00bf\u00c0\7")
        buf.write("\62\2\2\u00c0\u00c1\7d\2\2\u00c1\u00c6\7\62\2\2\u00c2")
        buf.write("\u00c3\7\62\2\2\u00c3\u00c4\7D\2\2\u00c4\u00c6\7\62\2")
        buf.write("\2\u00c5\u00bf\3\2\2\2\u00c5\u00c2\3\2\2\2\u00c6\u00c8")
        buf.write("\3\2\2\2\u00c7\u00aa\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8")
        buf.write("\n\3\2\2\2\u00c9\u00ca\t\5\2\2\u00ca\f\3\2\2\2\u00cb\u00cc")
        buf.write("\t\6\2\2\u00cc\16\3\2\2\2\u00cd\u00ce\t\7\2\2\u00ce\20")
        buf.write("\3\2\2\2\u00cf\u00d0\t\b\2\2\u00d0\22\3\2\2\2\u00d1\u00d2")
        buf.write("\5\25\13\2\u00d2\u00d3\5\27\f\2\u00d3\u00d4\b\n\6\2\u00d4")
        buf.write("\u00e2\3\2\2\2\u00d5\u00d6\5\25\13\2\u00d6\u00d7\5\31")
        buf.write("\r\2\u00d7\u00d8\b\n\7\2\u00d8\u00e2\3\2\2\2\u00d9\u00da")
        buf.write("\5\27\f\2\u00da\u00db\5\31\r\2\u00db\u00e2\3\2\2\2\u00dc")
        buf.write("\u00dd\5\25\13\2\u00dd\u00de\5\27\f\2\u00de\u00df\5\31")
        buf.write("\r\2\u00df\u00e0\b\n\b\2\u00e0\u00e2\3\2\2\2\u00e1\u00d1")
        buf.write("\3\2\2\2\u00e1\u00d5\3\2\2\2\u00e1\u00d9\3\2\2\2\u00e1")
        buf.write("\u00dc\3\2\2\2\u00e2\24\3\2\2\2\u00e3\u00e7\t\2\2\2\u00e4")
        buf.write("\u00e6\5\13\6\2\u00e5\u00e4\3\2\2\2\u00e6\u00e9\3\2\2")
        buf.write("\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00f2")
        buf.write("\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00ec\7a\2\2\u00eb")
        buf.write("\u00ed\5\13\6\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2")
        buf.write("\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1")
        buf.write("\3\2\2\2\u00f0\u00ea\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f7\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f5\u00f7\7\62\2\2\u00f6\u00e3")
        buf.write("\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\26\3\2\2\2\u00f8\u00fc")
        buf.write("\7\60\2\2\u00f9\u00fb\5\13\6\2\u00fa\u00f9\3\2\2\2\u00fb")
        buf.write("\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd\30\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0101\t\t")
        buf.write("\2\2\u0100\u0102\t\n\2\2\u0101\u0100\3\2\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0104\3\2\2\2\u0103\u0105\5\13\6\2\u0104")
        buf.write("\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107\32\3\2\2\2\u0108\u0109\7V\2")
        buf.write("\2\u0109\u010a\7t\2\2\u010a\u010b\7w\2\2\u010b\u0112\7")
        buf.write("g\2\2\u010c\u010d\7H\2\2\u010d\u010e\7c\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\u0110\7u\2\2\u0110\u0112\7g\2\2\u0111\u0108")
        buf.write("\3\2\2\2\u0111\u010c\3\2\2\2\u0112\34\3\2\2\2\u0113\u0117")
        buf.write("\7$\2\2\u0114\u0116\5\37\20\2\u0115\u0114\3\2\2\2\u0116")
        buf.write("\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2")
        buf.write("\u0118\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\7")
        buf.write("$\2\2\u011b\u011c\b\17\t\2\u011c\36\3\2\2\2\u011d\u0121")
        buf.write("\n\13\2\2\u011e\u0121\5!\21\2\u011f\u0121\5#\22\2\u0120")
        buf.write("\u011d\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u011f\3\2\2\2")
        buf.write("\u0121 \3\2\2\2\u0122\u0123\7^\2\2\u0123\u0124\t\f\2\2")
        buf.write("\u0124\"\3\2\2\2\u0125\u0126\7)\2\2\u0126\u0127\7$\2\2")
        buf.write("\u0127$\3\2\2\2\u0128\u0129\7^\2\2\u0129\u012c\n\f\2\2")
        buf.write("\u012a\u012c\n\r\2\2\u012b\u0128\3\2\2\2\u012b\u012a\3")
        buf.write("\2\2\2\u012c&\3\2\2\2\u012d\u012e\7E\2\2\u012e\u012f\7")
        buf.write("n\2\2\u012f\u0130\7c\2\2\u0130\u0131\7u\2\2\u0131\u0132")
        buf.write("\7u\2\2\u0132(\3\2\2\2\u0133\u0134\7C\2\2\u0134\u0135")
        buf.write("\7t\2\2\u0135\u0136\7t\2\2\u0136\u0137\7c\2\2\u0137\u0138")
        buf.write("\7{\2\2\u0138*\3\2\2\2\u0139\u013a\7X\2\2\u013a\u013b")
        buf.write("\7c\2\2\u013b\u013c\7t\2\2\u013c,\3\2\2\2\u013d\u013e")
        buf.write("\7X\2\2\u013e\u013f\7c\2\2\u013f\u0140\7n\2\2\u0140.\3")
        buf.write("\2\2\2\u0141\u0142\7*\2\2\u0142\60\3\2\2\2\u0143\u0144")
        buf.write("\7+\2\2\u0144\62\3\2\2\2\u0145\u0146\7}\2\2\u0146\64\3")
        buf.write("\2\2\2\u0147\u0148\7\177\2\2\u0148\66\3\2\2\2\u0149\u014a")
        buf.write("\7=\2\2\u014a8\3\2\2\2\u014b\u014c\7.\2\2\u014c:\3\2\2")
        buf.write("\2\u014d\u014e\7<\2\2\u014e<\3\2\2\2\u014f\u0150\7D\2")
        buf.write("\2\u0150\u0151\7q\2\2\u0151\u0152\7q\2\2\u0152\u0153\7")
        buf.write("n\2\2\u0153\u0154\7g\2\2\u0154\u0155\7c\2\2\u0155\u0156")
        buf.write("\7p\2\2\u0156>\3\2\2\2\u0157\u0158\7K\2\2\u0158\u0159")
        buf.write("\7p\2\2\u0159\u015a\7v\2\2\u015a@\3\2\2\2\u015b\u015c")
        buf.write("\7H\2\2\u015c\u015d\7n\2\2\u015d\u015e\7q\2\2\u015e\u015f")
        buf.write("\7c\2\2\u015f\u0160\7v\2\2\u0160B\3\2\2\2\u0161\u0162")
        buf.write("\7U\2\2\u0162\u0163\7v\2\2\u0163\u0164\7t\2\2\u0164\u0165")
        buf.write("\7k\2\2\u0165\u0166\7p\2\2\u0166\u0167\7i\2\2\u0167D\3")
        buf.write("\2\2\2\u0168\u016a\t\16\2\2\u0169\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u0170\3\2\2\2\u016d\u016f\t\17\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171F\3\2\2\2\u0172\u0170\3\2\2\2\u0173")
        buf.write("\u0174\7&\2\2\u0174H\3\2\2\2\u0175\u0177\5G$\2\u0176\u0178")
        buf.write("\t\16\2\2\u0177\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017e\3\2\2\2")
        buf.write("\u017b\u017d\t\17\2\2\u017c\u017b\3\2\2\2\u017d\u0180")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("J\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0183\t\20\2\2\u0182")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\b")
        buf.write("&\n\2\u0187L\3\2\2\2\u0188\u018c\7$\2\2\u0189\u018b\5")
        buf.write("\37\20\2\u018a\u0189\3\2\2\2\u018b\u018e\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018f\u0190\5O(\2\u0190\u0191\b\'")
        buf.write("\13\2\u0191N\3\2\2\2\u0192\u0194\t\21\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0194P\3\2\2\2\u0195\u0199\7$\2\2\u0196\u0198")
        buf.write("\5\37\20\2\u0197\u0196\3\2\2\2\u0198\u019b\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019c\3\2\2\2")
        buf.write("\u019b\u0199\3\2\2\2\u019c\u019d\5%\23\2\u019d\u019e\b")
        buf.write(")\f\2\u019eR\3\2\2\2\u019f\u01a0\13\2\2\2\u01a0\u01a1")
        buf.write("\b*\r\2\u01a1T\3\2\2\2-\2Y`diou|\u0080\u008a\u008c\u0093")
        buf.write("\u009a\u009e\u00a4\u00aa\u00b0\u00b7\u00bb\u00c5\u00c7")
        buf.write("\u00e1\u00e7\u00ee\u00f2\u00f6\u00fc\u0101\u0106\u0111")
        buf.write("\u0117\u0120\u012b\u0169\u016b\u016e\u0170\u0179\u017e")
        buf.write("\u0184\u018c\u0193\u0199\16\3\2\2\3\3\3\3\4\4\3\5\5\3")
        buf.write("\n\6\3\n\7\3\n\b\3\17\t\b\2\2\3\'\n\3)\13\3*\f")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER_LITERAL_X10 = 1
    INTEGER_LITERAL_X16 = 2
    INTEGER_LITERAL_X8 = 3
    INTEGER_LITERAL_X2 = 4
    FLOAT_LITERAL = 5
    BOOLEAN_LITERAL = 6
    STRING_LITERAL = 7
    CLASS = 8
    Array = 9
    VAR = 10
    VAL = 11
    LP = 12
    RP = 13
    LB = 14
    RB = 15
    SM = 16
    CM = 17
    COLON = 18
    BOOLEAN_TYP = 19
    INT_TYP = 20
    FLOAT_TYP = 21
    STRING_TYP = 22
    IDENTIFIER = 23
    STATIC_IDENTIFIER = 24
    WS = 25
    UNCLOSE_STRING = 26
    ILLEGAL_ESCAPE = 27
    ERROR_CHAR = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Class'", "'Array'", "'Var'", "'Val'", "'('", "')'", "'{'", 
            "'}'", "';'", "','", "':'", "'Boolean'", "'Int'", "'Float'", 
            "'String'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", "INTEGER_LITERAL_X8", 
            "INTEGER_LITERAL_X2", "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
            "CLASS", "Array", "VAR", "VAL", "LP", "RP", "LB", "RB", "SM", 
            "CM", "COLON", "BOOLEAN_TYP", "INT_TYP", "FLOAT_TYP", "STRING_TYP", 
            "IDENTIFIER", "STATIC_IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", "INTEGER_LITERAL_X8", 
                  "INTEGER_LITERAL_X2", "NUMBERDIGIT", "X16DIGIT", "X8DIGIT", 
                  "X2DIGIT", "FLOAT_LITERAL", "FLOAT_INT_COMPO", "FLOAT_DECIMAL_COMPO", 
                  "FLOAT_EXPO_COMPO", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                  "CHARACTER", "ESCAPE_CHAR", "DOUBLE_QUOTE_IN_STRING", 
                  "ESCAPE_CHAR_ILEGAL", "CLASS", "Array", "VAR", "VAL", 
                  "LP", "RP", "LB", "RB", "SM", "CM", "COLON", "BOOLEAN_TYP", 
                  "INT_TYP", "FLOAT_TYP", "STRING_TYP", "IDENTIFIER", "DOLAR_SIGN", 
                  "STATIC_IDENTIFIER", "WS", "UNCLOSE_STRING", "END_A_LINE_SIGN", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INTEGER_LITERAL_X10_action 
            actions[1] = self.INTEGER_LITERAL_X16_action 
            actions[2] = self.INTEGER_LITERAL_X8_action 
            actions[3] = self.INTEGER_LITERAL_X2_action 
            actions[8] = self.FLOAT_LITERAL_action 
            actions[13] = self.STRING_LITERAL_action 
            actions[37] = self.UNCLOSE_STRING_action 
            actions[39] = self.ILLEGAL_ESCAPE_action 
            actions[40] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LITERAL_X10_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text.replace("_","")
     

    def INTEGER_LITERAL_X16_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text=self.text.replace("_","") 
     

    def INTEGER_LITERAL_X8_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text=self.text.replace("_","") 
     

    def INTEGER_LITERAL_X2_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             self.text=self.text.replace("_","") 
     

    def FLOAT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
             self.text=self.text.replace("_","") 
     

        if actionIndex == 5:
             self.text=self.text.replace("_","") 
     

        if actionIndex == 6:
             self.text=self.text.replace("_","") 
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            		inputstr=str(self.text)
            		self.text=inputstr[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
             
            		unclose_str=str(self.text)
            		raise UncloseString(unclose_str[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

            		ilegal = str(self.text)
            		raise IllegalEscape(ilegal[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:

            		raise ErrorToken(self.text)
            	
     


