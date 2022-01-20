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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("\u0086\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\6\7]\n\7\r\7\16\7^\3\b\3\b\3\t\3\t\3\n\6\nf\n")
        buf.write("\n\r\n\16\ng\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\6\23{\n\23\r")
        buf.write("\23\16\23|\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\2\2")
        buf.write("\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27\3\2")
        buf.write("\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2\u0088\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5\62\3\2")
        buf.write("\2\2\7C\3\2\2\2\tM\3\2\2\2\13U\3\2\2\2\r\\\3\2\2\2\17")
        buf.write("`\3\2\2\2\21b\3\2\2\2\23e\3\2\2\2\25i\3\2\2\2\27k\3\2")
        buf.write("\2\2\31m\3\2\2\2\33o\3\2\2\2\35q\3\2\2\2\37s\3\2\2\2!")
        buf.write("u\3\2\2\2#w\3\2\2\2%z\3\2\2\2\'\u0080\3\2\2\2)\u0082\3")
        buf.write("\2\2\2+\u0084\3\2\2\2-.\7o\2\2./\7c\2\2/\60\7k\2\2\60")
        buf.write("\61\7p\2\2\61\4\3\2\2\2\62\63\7r\2\2\63\64\7t\2\2\64\65")
        buf.write("\7q\2\2\65\66\7i\2\2\66\67\7t\2\2\678\7c\2\289\7o\2\2")
        buf.write("9:\7e\2\2:;\7n\2\2;<\7c\2\2<=\7u\2\2=>\7u\2\2>?\7d\2\2")
        buf.write("?@\7q\2\2@A\7f\2\2AB\7{\2\2B\6\3\2\2\2CD\7e\2\2DE\7n\2")
        buf.write("\2EF\7c\2\2FG\7u\2\2GH\7u\2\2HI\7d\2\2IJ\7q\2\2JK\7f\2")
        buf.write("\2KL\7{\2\2L\b\3\2\2\2MN\7R\2\2NO\7t\2\2OP\7q\2\2PQ\7")
        buf.write("i\2\2QR\7t\2\2RS\7c\2\2ST\7o\2\2T\n\3\2\2\2UV\7E\2\2V")
        buf.write("W\7n\2\2WX\7c\2\2XY\7u\2\2YZ\7u\2\2Z\f\3\2\2\2[]\t\2\2")
        buf.write("\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\16\3\2\2")
        buf.write("\2`a\t\2\2\2a\20\3\2\2\2bc\t\3\2\2c\22\3\2\2\2df\t\3\2")
        buf.write("\2ed\3\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\24\3\2\2\2")
        buf.write("ij\7a\2\2j\26\3\2\2\2kl\7}\2\2l\30\3\2\2\2mn\7\177\2\2")
        buf.write("n\32\3\2\2\2op\7*\2\2p\34\3\2\2\2qr\7+\2\2r\36\3\2\2\2")
        buf.write("st\7=\2\2t \3\2\2\2uv\7.\2\2v\"\3\2\2\2wx\7<\2\2x$\3\2")
        buf.write("\2\2y{\t\4\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2")
        buf.write("}~\3\2\2\2~\177\b\23\2\2\177&\3\2\2\2\u0080\u0081\13\2")
        buf.write("\2\2\u0081(\3\2\2\2\u0082\u0083\13\2\2\2\u0083*\3\2\2")
        buf.write("\2\u0084\u0085\13\2\2\2\u0085,\3\2\2\2\6\2^g|\3\b\2\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    CHAR_SEQ = 6
    CHAR = 7
    NUM = 8
    NUM_SEQ = 9
    UNDERCORE = 10
    LB = 11
    RB = 12
    LP = 13
    RP = 14
    SM = 15
    CM = 16
    COLON = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'programclassbody'", "'classbody'", "'Program'", 
            "'Class'", "'_'", "'{'", "'}'", "'('", "')'", "';'", "','", 
            "':'" ]

    symbolicNames = [ "<INVALID>",
            "CHAR_SEQ", "CHAR", "NUM", "NUM_SEQ", "UNDERCORE", "LB", "RB", 
            "LP", "RP", "SM", "CM", "COLON", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "CHAR_SEQ", "CHAR", 
                  "NUM", "NUM_SEQ", "UNDERCORE", "LB", "RB", "LP", "RP", 
                  "SM", "CM", "COLON", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


