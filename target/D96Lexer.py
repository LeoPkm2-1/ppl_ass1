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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 ")
        buf.write("\u01af\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\3\3\3")
        buf.write("\7\3\\\n\3\f\3\16\3_\13\3\3\3\3\3\6\3c\n\3\r\3\16\3d\7")
        buf.write("\3g\n\3\f\3\16\3j\13\3\3\3\3\3\5\3n\n\3\3\4\3\4\3\4\3")
        buf.write("\4\5\4t\n\4\3\4\3\4\7\4x\n\4\f\4\16\4{\13\4\3\4\3\4\6")
        buf.write("\4\177\n\4\r\4\16\4\u0080\7\4\u0083\n\4\f\4\16\4\u0086")
        buf.write("\13\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u008f\n\4\5\4\u0091")
        buf.write("\n\4\3\5\3\5\3\5\7\5\u0096\n\5\f\5\16\5\u0099\13\5\3\5")
        buf.write("\3\5\6\5\u009d\n\5\r\5\16\5\u009e\7\5\u00a1\n\5\f\5\16")
        buf.write("\5\u00a4\13\5\3\5\3\5\3\5\5\5\u00a9\n\5\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u00af\n\6\3\6\3\6\7\6\u00b3\n\6\f\6\16\6\u00b6")
        buf.write("\13\6\3\6\3\6\6\6\u00ba\n\6\r\6\16\6\u00bb\7\6\u00be\n")
        buf.write("\6\f\6\16\6\u00c1\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u00ca\n\6\5\6\u00cc\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\5\13\u00e6\n\13\3\f\3\f\7")
        buf.write("\f\u00ea\n\f\f\f\16\f\u00ed\13\f\3\f\3\f\6\f\u00f1\n\f")
        buf.write("\r\f\16\f\u00f2\7\f\u00f5\n\f\f\f\16\f\u00f8\13\f\3\f")
        buf.write("\5\f\u00fb\n\f\3\r\3\r\7\r\u00ff\n\r\f\r\16\r\u0102\13")
        buf.write("\r\3\16\3\16\5\16\u0106\n\16\3\16\6\16\u0109\n\16\r\16")
        buf.write("\16\16\u010a\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\5\17\u0116\n\17\3\20\3\20\7\20\u011a\n\20\f\20\16")
        buf.write("\20\u011d\13\20\3\20\3\20\3\20\3\21\3\21\3\21\5\21\u0125")
        buf.write("\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\5\24")
        buf.write("\u0130\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\6")
        buf.write("$\u016e\n$\r$\16$\u016f\3$\7$\u0173\n$\f$\16$\u0176\13")
        buf.write("$\3%\6%\u0179\n%\r%\16%\u017a\3%\7%\u017e\n%\f%\16%\u0181")
        buf.write("\13%\3&\3&\6&\u0185\n&\r&\16&\u0186\3&\7&\u018a\n&\f&")
        buf.write("\16&\u018d\13&\3\'\6\'\u0190\n\'\r\'\16\'\u0191\3\'\3")
        buf.write("\'\3(\3(\7(\u0198\n(\f(\16(\u019b\13(\3(\3(\3(\3)\5)\u01a1")
        buf.write("\n)\3*\3*\7*\u01a5\n*\f*\16*\u01a8\13*\3*\3*\3*\3+\3+")
        buf.write("\3+\2\2,\3\3\5\4\7\5\t\6\13\7\r\2\17\2\21\2\23\2\25\b")
        buf.write("\27\2\31\2\33\2\35\t\37\n!\2#\2%\2\'\2)\13+\f-\r/\16\61")
        buf.write("\17\63\20\65\21\67\229\23;\24=\25?\26A\27C\30E\31G\32")
        buf.write("I\33K\34M\35O\36Q\2S\37U \3\2\22\3\2\63;\4\2\63;CH\3\2")
        buf.write("\639\3\2\62;\4\2\62;CH\3\2\629\3\2\62\63\4\2GGgg\4\2-")
        buf.write("-//\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2^^\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\7\3\n\f\16\17$")
        buf.write("$))^^\2\u01ce\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\25\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\3W\3\2\2\2\5")
        buf.write("m\3\2\2\2\7\u0090\3\2\2\2\t\u00a8\3\2\2\2\13\u00cb\3\2")
        buf.write("\2\2\r\u00cd\3\2\2\2\17\u00cf\3\2\2\2\21\u00d1\3\2\2\2")
        buf.write("\23\u00d3\3\2\2\2\25\u00e5\3\2\2\2\27\u00fa\3\2\2\2\31")
        buf.write("\u00fc\3\2\2\2\33\u0103\3\2\2\2\35\u0115\3\2\2\2\37\u0117")
        buf.write("\3\2\2\2!\u0124\3\2\2\2#\u0126\3\2\2\2%\u0129\3\2\2\2")
        buf.write("\'\u012f\3\2\2\2)\u0131\3\2\2\2+\u0137\3\2\2\2-\u013d")
        buf.write("\3\2\2\2/\u013f\3\2\2\2\61\u0141\3\2\2\2\63\u0143\3\2")
        buf.write("\2\2\65\u0145\3\2\2\2\67\u0147\3\2\2\29\u0149\3\2\2\2")
        buf.write(";\u014b\3\2\2\2=\u014f\3\2\2\2?\u0153\3\2\2\2A\u015b\3")
        buf.write("\2\2\2C\u015f\3\2\2\2E\u0165\3\2\2\2G\u016d\3\2\2\2I\u0178")
        buf.write("\3\2\2\2K\u0182\3\2\2\2M\u018f\3\2\2\2O\u0195\3\2\2\2")
        buf.write("Q\u01a0\3\2\2\2S\u01a2\3\2\2\2U\u01ac\3\2\2\2WX\7?\2\2")
        buf.write("X\4\3\2\2\2Y]\t\2\2\2Z\\\5\r\7\2[Z\3\2\2\2\\_\3\2\2\2")
        buf.write("][\3\2\2\2]^\3\2\2\2^h\3\2\2\2_]\3\2\2\2`b\7a\2\2ac\5")
        buf.write("\r\7\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2eg\3\2\2")
        buf.write("\2f`\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2ik\3\2\2\2j")
        buf.write("h\3\2\2\2kn\b\3\2\2ln\7\62\2\2mY\3\2\2\2ml\3\2\2\2n\6")
        buf.write("\3\2\2\2op\7\62\2\2pt\7z\2\2qr\7\62\2\2rt\7Z\2\2so\3\2")
        buf.write("\2\2sq\3\2\2\2tu\3\2\2\2uy\t\3\2\2vx\5\17\b\2wv\3\2\2")
        buf.write("\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\u0084\3\2\2\2{y\3\2")
        buf.write("\2\2|~\7a\2\2}\177\5\17\b\2~}\3\2\2\2\177\u0080\3\2\2")
        buf.write("\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0083\3\2")
        buf.write("\2\2\u0082|\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3")
        buf.write("\2\2\2\u0084\u0085\3\2\2\2\u0085\u0087\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0087\u0091\b\4\3\2\u0088\u0089\7\62\2\2\u0089")
        buf.write("\u008a\7z\2\2\u008a\u008f\7\62\2\2\u008b\u008c\7\62\2")
        buf.write("\2\u008c\u008d\7Z\2\2\u008d\u008f\7\62\2\2\u008e\u0088")
        buf.write("\3\2\2\2\u008e\u008b\3\2\2\2\u008f\u0091\3\2\2\2\u0090")
        buf.write("s\3\2\2\2\u0090\u008e\3\2\2\2\u0091\b\3\2\2\2\u0092\u0093")
        buf.write("\7\62\2\2\u0093\u0097\t\4\2\2\u0094\u0096\5\21\t\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u00a2\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u009a\u009c\7a\2\2\u009b\u009d\5\21\t\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009a\3\2\2\2")
        buf.write("\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3")
        buf.write("\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a9")
        buf.write("\b\5\4\2\u00a6\u00a7\7\62\2\2\u00a7\u00a9\7\62\2\2\u00a8")
        buf.write("\u0092\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\n\3\2\2\2\u00aa")
        buf.write("\u00ab\7\62\2\2\u00ab\u00af\7d\2\2\u00ac\u00ad\7\62\2")
        buf.write("\2\u00ad\u00af\7D\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b4\7\63\2\2\u00b1")
        buf.write("\u00b3\5\23\n\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2")
        buf.write("\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00bf")
        buf.write("\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b9\7a\2\2\u00b8")
        buf.write("\u00ba\5\23\n\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2")
        buf.write("\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be")
        buf.write("\3\2\2\2\u00bd\u00b7\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2")
        buf.write("\u00c1\u00bf\3\2\2\2\u00c2\u00cc\b\6\5\2\u00c3\u00c4\7")
        buf.write("\62\2\2\u00c4\u00c5\7d\2\2\u00c5\u00ca\7\62\2\2\u00c6")
        buf.write("\u00c7\7\62\2\2\u00c7\u00c8\7D\2\2\u00c8\u00ca\7\62\2")
        buf.write("\2\u00c9\u00c3\3\2\2\2\u00c9\u00c6\3\2\2\2\u00ca\u00cc")
        buf.write("\3\2\2\2\u00cb\u00ae\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc")
        buf.write("\f\3\2\2\2\u00cd\u00ce\t\5\2\2\u00ce\16\3\2\2\2\u00cf")
        buf.write("\u00d0\t\6\2\2\u00d0\20\3\2\2\2\u00d1\u00d2\t\7\2\2\u00d2")
        buf.write("\22\3\2\2\2\u00d3\u00d4\t\b\2\2\u00d4\24\3\2\2\2\u00d5")
        buf.write("\u00d6\5\27\f\2\u00d6\u00d7\5\31\r\2\u00d7\u00d8\b\13")
        buf.write("\6\2\u00d8\u00e6\3\2\2\2\u00d9\u00da\5\27\f\2\u00da\u00db")
        buf.write("\5\33\16\2\u00db\u00dc\b\13\7\2\u00dc\u00e6\3\2\2\2\u00dd")
        buf.write("\u00de\5\31\r\2\u00de\u00df\5\33\16\2\u00df\u00e6\3\2")
        buf.write("\2\2\u00e0\u00e1\5\27\f\2\u00e1\u00e2\5\31\r\2\u00e2\u00e3")
        buf.write("\5\33\16\2\u00e3\u00e4\b\13\b\2\u00e4\u00e6\3\2\2\2\u00e5")
        buf.write("\u00d5\3\2\2\2\u00e5\u00d9\3\2\2\2\u00e5\u00dd\3\2\2\2")
        buf.write("\u00e5\u00e0\3\2\2\2\u00e6\26\3\2\2\2\u00e7\u00eb\t\2")
        buf.write("\2\2\u00e8\u00ea\5\r\7\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00f6\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f0\7a\2\2")
        buf.write("\u00ef\u00f1\5\r\7\2\u00f0\u00ef\3\2\2\2\u00f1\u00f2\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5")
        buf.write("\3\2\2\2\u00f4\u00ee\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00fb\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f9\u00fb\7\62\2\2\u00fa\u00e7")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\30\3\2\2\2\u00fc\u0100")
        buf.write("\7\60\2\2\u00fd\u00ff\5\r\7\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write("\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\32\3\2\2\2\u0102\u0100\3\2\2\2\u0103\u0105\t\t")
        buf.write("\2\2\u0104\u0106\t\n\2\2\u0105\u0104\3\2\2\2\u0105\u0106")
        buf.write("\3\2\2\2\u0106\u0108\3\2\2\2\u0107\u0109\5\r\7\2\u0108")
        buf.write("\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0108\3\2\2\2")
        buf.write("\u010a\u010b\3\2\2\2\u010b\34\3\2\2\2\u010c\u010d\7V\2")
        buf.write("\2\u010d\u010e\7t\2\2\u010e\u010f\7w\2\2\u010f\u0116\7")
        buf.write("g\2\2\u0110\u0111\7H\2\2\u0111\u0112\7c\2\2\u0112\u0113")
        buf.write("\7n\2\2\u0113\u0114\7u\2\2\u0114\u0116\7g\2\2\u0115\u010c")
        buf.write("\3\2\2\2\u0115\u0110\3\2\2\2\u0116\36\3\2\2\2\u0117\u011b")
        buf.write("\7$\2\2\u0118\u011a\5!\21\2\u0119\u0118\3\2\2\2\u011a")
        buf.write("\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7")
        buf.write("$\2\2\u011f\u0120\b\20\t\2\u0120 \3\2\2\2\u0121\u0125")
        buf.write("\n\13\2\2\u0122\u0125\5#\22\2\u0123\u0125\5%\23\2\u0124")
        buf.write("\u0121\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0123\3\2\2\2")
        buf.write("\u0125\"\3\2\2\2\u0126\u0127\7^\2\2\u0127\u0128\t\f\2")
        buf.write("\2\u0128$\3\2\2\2\u0129\u012a\7)\2\2\u012a\u012b\7$\2")
        buf.write("\2\u012b&\3\2\2\2\u012c\u012d\7^\2\2\u012d\u0130\n\f\2")
        buf.write("\2\u012e\u0130\n\r\2\2\u012f\u012c\3\2\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u0130(\3\2\2\2\u0131\u0132\7C\2\2\u0132\u0133")
        buf.write("\7t\2\2\u0133\u0134\7t\2\2\u0134\u0135\7c\2\2\u0135\u0136")
        buf.write("\7{\2\2\u0136*\3\2\2\2\u0137\u0138\7E\2\2\u0138\u0139")
        buf.write("\7n\2\2\u0139\u013a\7c\2\2\u013a\u013b\7u\2\2\u013b\u013c")
        buf.write("\7u\2\2\u013c,\3\2\2\2\u013d\u013e\7*\2\2\u013e.\3\2\2")
        buf.write("\2\u013f\u0140\7+\2\2\u0140\60\3\2\2\2\u0141\u0142\7}")
        buf.write("\2\2\u0142\62\3\2\2\2\u0143\u0144\7\177\2\2\u0144\64\3")
        buf.write("\2\2\2\u0145\u0146\7=\2\2\u0146\66\3\2\2\2\u0147\u0148")
        buf.write("\7.\2\2\u01488\3\2\2\2\u0149\u014a\7<\2\2\u014a:\3\2\2")
        buf.write("\2\u014b\u014c\7X\2\2\u014c\u014d\7c\2\2\u014d\u014e\7")
        buf.write("n\2\2\u014e<\3\2\2\2\u014f\u0150\7X\2\2\u0150\u0151\7")
        buf.write("c\2\2\u0151\u0152\7t\2\2\u0152>\3\2\2\2\u0153\u0154\7")
        buf.write("D\2\2\u0154\u0155\7q\2\2\u0155\u0156\7q\2\2\u0156\u0157")
        buf.write("\7n\2\2\u0157\u0158\7g\2\2\u0158\u0159\7c\2\2\u0159\u015a")
        buf.write("\7p\2\2\u015a@\3\2\2\2\u015b\u015c\7K\2\2\u015c\u015d")
        buf.write("\7p\2\2\u015d\u015e\7v\2\2\u015eB\3\2\2\2\u015f\u0160")
        buf.write("\7H\2\2\u0160\u0161\7n\2\2\u0161\u0162\7q\2\2\u0162\u0163")
        buf.write("\7c\2\2\u0163\u0164\7v\2\2\u0164D\3\2\2\2\u0165\u0166")
        buf.write("\7U\2\2\u0166\u0167\7v\2\2\u0167\u0168\7t\2\2\u0168\u0169")
        buf.write("\7k\2\2\u0169\u016a\7p\2\2\u016a\u016b\7i\2\2\u016bF\3")
        buf.write("\2\2\2\u016c\u016e\t\16\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0174\3\2\2\2\u0171\u0173\t\17\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175H\3\2\2\2\u0176\u0174\3\2\2\2\u0177")
        buf.write("\u0179\t\16\2\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2")
        buf.write("\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017f")
        buf.write("\3\2\2\2\u017c\u017e\t\17\2\2\u017d\u017c\3\2\2\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180J\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0184\7&\2\2")
        buf.write("\u0183\u0185\t\16\2\2\u0184\u0183\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u018b\3\2\2\2\u0188\u018a\t\17\2\2\u0189\u0188\3\2\2")
        buf.write("\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018cL\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u0190")
        buf.write("\t\20\2\2\u018f\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193\u0194\b\'\n\2\u0194N\3\2\2\2\u0195\u0199\7$\2\2")
        buf.write("\u0196\u0198\5!\21\2\u0197\u0196\3\2\2\2\u0198\u019b\3")
        buf.write("\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019c")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u019d\5Q)\2\u019d\u019e")
        buf.write("\b(\13\2\u019eP\3\2\2\2\u019f\u01a1\t\21\2\2\u01a0\u019f")
        buf.write("\3\2\2\2\u01a1R\3\2\2\2\u01a2\u01a6\7$\2\2\u01a3\u01a5")
        buf.write("\5!\21\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2")
        buf.write("\u01a8\u01a6\3\2\2\2\u01a9\u01aa\5\'\24\2\u01aa\u01ab")
        buf.write("\b*\f\2\u01abT\3\2\2\2\u01ac\u01ad\13\2\2\2\u01ad\u01ae")
        buf.write("\b+\r\2\u01aeV\3\2\2\2-\2]dhmsy\u0080\u0084\u008e\u0090")
        buf.write("\u0097\u009e\u00a2\u00a8\u00ae\u00b4\u00bb\u00bf\u00c9")
        buf.write("\u00cb\u00e5\u00eb\u00f2\u00f6\u00fa\u0100\u0105\u010a")
        buf.write("\u0115\u011b\u0124\u012f\u016f\u0174\u017a\u017f\u0186")
        buf.write("\u018b\u0191\u0199\u01a0\u01a6\16\3\3\2\3\4\3\3\5\4\3")
        buf.write("\6\5\3\13\6\3\13\7\3\13\b\3\20\t\b\2\2\3(\n\3*\13\3+\f")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTEGER_LITERAL_X10 = 2
    INTEGER_LITERAL_X16 = 3
    INTEGER_LITERAL_X8 = 4
    INTEGER_LITERAL_X2 = 5
    FLOAT_LITERAL = 6
    BOOLEAN_LITERAL = 7
    STRING_LITERAL = 8
    Array = 9
    CLASS = 10
    LP = 11
    RP = 12
    LB = 13
    RB = 14
    SM = 15
    CM = 16
    COLON = 17
    VAL = 18
    VAR = 19
    BOOLEAN_TYP = 20
    INT_TYP = 21
    FLOAT_TYP = 22
    STRING_TYP = 23
    IDENTIFIER = 24
    CLASSNAME = 25
    STATIC_IDENTIFIER = 26
    WS = 27
    UNCLOSE_STRING = 28
    ILLEGAL_ESCAPE = 29
    ERROR_CHAR = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'Array'", "'Class'", "'('", "')'", "'{'", "'}'", "';'", 
            "','", "':'", "'Val'", "'Var'", "'Boolean'", "'Int'", "'Float'", 
            "'String'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", "INTEGER_LITERAL_X8", 
            "INTEGER_LITERAL_X2", "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
            "Array", "CLASS", "LP", "RP", "LB", "RB", "SM", "CM", "COLON", 
            "VAL", "VAR", "BOOLEAN_TYP", "INT_TYP", "FLOAT_TYP", "STRING_TYP", 
            "IDENTIFIER", "CLASSNAME", "STATIC_IDENTIFIER", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", 
                  "INTEGER_LITERAL_X8", "INTEGER_LITERAL_X2", "NUMBERDIGIT", 
                  "X16DIGIT", "X8DIGIT", "X2DIGIT", "FLOAT_LITERAL", "FLOAT_INT_COMPO", 
                  "FLOAT_DECIMAL_COMPO", "FLOAT_EXPO_COMPO", "BOOLEAN_LITERAL", 
                  "STRING_LITERAL", "CHARACTER", "ESCAPE_CHAR", "DOUBLE_QUOTE_IN_STRING", 
                  "ESCAPE_CHAR_ILEGAL", "Array", "CLASS", "LP", "RP", "LB", 
                  "RB", "SM", "CM", "COLON", "VAL", "VAR", "BOOLEAN_TYP", 
                  "INT_TYP", "FLOAT_TYP", "STRING_TYP", "IDENTIFIER", "CLASSNAME", 
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
            actions[1] = self.INTEGER_LITERAL_X10_action 
            actions[2] = self.INTEGER_LITERAL_X16_action 
            actions[3] = self.INTEGER_LITERAL_X8_action 
            actions[4] = self.INTEGER_LITERAL_X2_action 
            actions[9] = self.FLOAT_LITERAL_action 
            actions[14] = self.STRING_LITERAL_action 
            actions[38] = self.UNCLOSE_STRING_action 
            actions[40] = self.ILLEGAL_ESCAPE_action 
            actions[41] = self.ERROR_CHAR_action 
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
            	
     


