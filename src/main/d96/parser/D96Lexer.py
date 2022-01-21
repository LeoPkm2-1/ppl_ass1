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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32")
        buf.write("\u00d8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\7\6_\n\6\f\6\16\6b\13\6\3\6\3\6\6")
        buf.write("\6f\n\6\r\6\16\6g\7\6j\n\6\f\6\16\6m\13\6\3\6\3\6\5\6")
        buf.write("q\n\6\3\7\3\7\6\7u\n\7\r\7\16\7v\3\7\3\7\6\7{\n\7\r\7")
        buf.write("\16\7|\7\7\177\n\7\f\7\16\7\u0082\13\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\6\b\u0089\n\b\r\b\16\b\u008a\3\b\3\b\6\b\u008f\n")
        buf.write("\b\r\b\16\b\u0090\7\b\u0093\n\b\f\b\16\b\u0096\13\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\6\t\u009d\n\t\r\t\16\t\u009e\3\t\3")
        buf.write("\t\6\t\u00a3\n\t\r\t\16\t\u00a4\7\t\u00a7\n\t\f\t\16\t")
        buf.write("\u00aa\13\t\3\t\3\t\3\n\6\n\u00af\n\n\r\n\16\n\u00b0\3")
        buf.write("\13\3\13\3\f\3\f\3\r\6\r\u00b8\n\r\r\r\16\r\u00b9\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\6\26\u00cd\n\26\r\26\16\26\u00ce")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\2\2\32\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\3\2\13\3\2\63;\3\2\62;\3\2\629\4\2ZZzz\4\2\62;CH\4\2")
        buf.write("DDdd\3\2\62\63\4\2C\\c|\5\2\13\f\17\17\"\"\2\u00e7\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\3\63\3\2\2\2\5D\3\2\2\2\7N\3\2")
        buf.write("\2\2\tV\3\2\2\2\13p\3\2\2\2\rr\3\2\2\2\17\u0085\3\2\2")
        buf.write("\2\21\u0099\3\2\2\2\23\u00ae\3\2\2\2\25\u00b2\3\2\2\2")
        buf.write("\27\u00b4\3\2\2\2\31\u00b7\3\2\2\2\33\u00bb\3\2\2\2\35")
        buf.write("\u00bd\3\2\2\2\37\u00bf\3\2\2\2!\u00c1\3\2\2\2#\u00c3")
        buf.write("\3\2\2\2%\u00c5\3\2\2\2\'\u00c7\3\2\2\2)\u00c9\3\2\2\2")
        buf.write("+\u00cc\3\2\2\2-\u00d2\3\2\2\2/\u00d4\3\2\2\2\61\u00d6")
        buf.write("\3\2\2\2\63\64\7r\2\2\64\65\7t\2\2\65\66\7q\2\2\66\67")
        buf.write("\7i\2\2\678\7t\2\289\7c\2\29:\7o\2\2:;\7e\2\2;<\7n\2\2")
        buf.write("<=\7c\2\2=>\7u\2\2>?\7u\2\2?@\7d\2\2@A\7q\2\2AB\7f\2\2")
        buf.write("BC\7{\2\2C\4\3\2\2\2DE\7e\2\2EF\7n\2\2FG\7c\2\2GH\7u\2")
        buf.write("\2HI\7u\2\2IJ\7d\2\2JK\7q\2\2KL\7f\2\2LM\7{\2\2M\6\3\2")
        buf.write("\2\2NO\7R\2\2OP\7t\2\2PQ\7q\2\2QR\7i\2\2RS\7t\2\2ST\7")
        buf.write("c\2\2TU\7o\2\2U\b\3\2\2\2VW\7E\2\2WX\7n\2\2XY\7c\2\2Y")
        buf.write("Z\7u\2\2Z[\7u\2\2[\n\3\2\2\2\\`\t\2\2\2]_\t\3\2\2^]\3")
        buf.write("\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ak\3\2\2\2b`\3\2\2")
        buf.write("\2ce\7a\2\2df\t\3\2\2ed\3\2\2\2fg\3\2\2\2ge\3\2\2\2gh")
        buf.write("\3\2\2\2hj\3\2\2\2ic\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2")
        buf.write("\2\2ln\3\2\2\2mk\3\2\2\2nq\b\6\2\2oq\7\62\2\2p\\\3\2\2")
        buf.write("\2po\3\2\2\2q\f\3\2\2\2rt\7\62\2\2su\t\3\2\2ts\3\2\2\2")
        buf.write("uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\u0080\3\2\2\2xz\7a\2\2")
        buf.write("y{\t\4\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\177")
        buf.write("\3\2\2\2~x\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2\2")
        buf.write("\u0083\u0084\b\7\3\2\u0084\16\3\2\2\2\u0085\u0086\7\62")
        buf.write("\2\2\u0086\u0088\t\5\2\2\u0087\u0089\t\6\2\2\u0088\u0087")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u008b\3\2\2\2\u008b\u0094\3\2\2\2\u008c\u008e\7a\2\2")
        buf.write("\u008d\u008f\t\6\2\2\u008e\u008d\3\2\2\2\u008f\u0090\3")
        buf.write("\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093")
        buf.write("\3\2\2\2\u0092\u008c\3\2\2\2\u0093\u0096\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2")
        buf.write("\u0096\u0094\3\2\2\2\u0097\u0098\b\b\4\2\u0098\20\3\2")
        buf.write("\2\2\u0099\u009a\7\62\2\2\u009a\u009c\t\7\2\2\u009b\u009d")
        buf.write("\t\b\2\2\u009c\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a8\3\2\2\2")
        buf.write("\u00a0\u00a2\7a\2\2\u00a1\u00a3\t\b\2\2\u00a2\u00a1\3")
        buf.write("\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a0\3\2\2\2\u00a7")
        buf.write("\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ac\b")
        buf.write("\t\5\2\u00ac\22\3\2\2\2\u00ad\u00af\t\t\2\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\24\3\2\2\2\u00b2\u00b3\t\t\2\2\u00b3")
        buf.write("\26\3\2\2\2\u00b4\u00b5\t\3\2\2\u00b5\30\3\2\2\2\u00b6")
        buf.write("\u00b8\t\3\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2")
        buf.write("\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\32\3\2")
        buf.write("\2\2\u00bb\u00bc\7a\2\2\u00bc\34\3\2\2\2\u00bd\u00be\7")
        buf.write("}\2\2\u00be\36\3\2\2\2\u00bf\u00c0\7\177\2\2\u00c0 \3")
        buf.write("\2\2\2\u00c1\u00c2\7*\2\2\u00c2\"\3\2\2\2\u00c3\u00c4")
        buf.write("\7+\2\2\u00c4$\3\2\2\2\u00c5\u00c6\7=\2\2\u00c6&\3\2\2")
        buf.write("\2\u00c7\u00c8\7.\2\2\u00c8(\3\2\2\2\u00c9\u00ca\7<\2")
        buf.write("\2\u00ca*\3\2\2\2\u00cb\u00cd\t\n\2\2\u00cc\u00cb\3\2")
        buf.write("\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\b\26\6\2\u00d1")
        buf.write(",\3\2\2\2\u00d2\u00d3\13\2\2\2\u00d3.\3\2\2\2\u00d4\u00d5")
        buf.write("\13\2\2\2\u00d5\60\3\2\2\2\u00d6\u00d7\13\2\2\2\u00d7")
        buf.write("\62\3\2\2\2\23\2`gkpv|\u0080\u008a\u0090\u0094\u009e\u00a4")
        buf.write("\u00a8\u00b0\u00b9\u00ce\7\3\6\2\3\7\3\3\b\4\3\t\5\b\2")
        buf.write("\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INT_DEC = 5
    INT_OCT = 6
    INT_HEX = 7
    INT_BIN = 8
    CHAR_SEQ = 9
    CHAR = 10
    NUM = 11
    NUM_SEQ = 12
    UNDERCORE = 13
    LB = 14
    RB = 15
    LP = 16
    RP = 17
    SM = 18
    CM = 19
    COLON = 20
    WS = 21
    ERROR_CHAR = 22
    UNCLOSE_STRING = 23
    ILLEGAL_ESCAPE = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'programclassbody'", "'classbody'", "'Program'", "'Class'", 
            "'_'", "'{'", "'}'", "'('", "')'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "INT_DEC", "INT_OCT", "INT_HEX", "INT_BIN", "CHAR_SEQ", "CHAR", 
            "NUM", "NUM_SEQ", "UNDERCORE", "LB", "RB", "LP", "RP", "SM", 
            "CM", "COLON", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INT_DEC", "INT_OCT", 
                  "INT_HEX", "INT_BIN", "CHAR_SEQ", "CHAR", "NUM", "NUM_SEQ", 
                  "UNDERCORE", "LB", "RB", "LP", "RP", "SM", "CM", "COLON", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[4] = self.INT_DEC_action 
            actions[5] = self.INT_OCT_action 
            actions[6] = self.INT_HEX_action 
            actions[7] = self.INT_BIN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_DEC_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text=self.text.replace("_","") 
     

    def INT_OCT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text=self.text.replace("_","") 
     

    def INT_HEX_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text=self.text.replace("_","") 
     

    def INT_BIN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             self.text=self.text.replace("_","") 
     


