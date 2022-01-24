# Generated from e:\UserD\Documents\studying\PPL\ASS\ass1\initial\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("\u00dd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\7\2&")
        buf.write("\n\2\f\2\16\2)\13\2\3\2\3\2\6\2-\n\2\r\2\16\2.\7\2\61")
        buf.write("\n\2\f\2\16\2\64\13\2\3\2\3\2\5\28\n\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3>\n\3\3\3\3\3\7\3B\n\3\f\3\16\3E\13\3\3\3\3\3\6\3")
        buf.write("I\n\3\r\3\16\3J\7\3M\n\3\f\3\16\3P\13\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3Y\n\3\5\3[\n\3\3\4\3\4\3\4\7\4`\n\4")
        buf.write("\f\4\16\4c\13\4\3\4\3\4\6\4g\n\4\r\4\16\4h\7\4k\n\4\f")
        buf.write("\4\16\4n\13\4\3\4\3\4\3\4\5\4s\n\4\3\5\3\5\3\5\3\5\5\5")
        buf.write("y\n\5\3\5\3\5\7\5}\n\5\f\5\16\5\u0080\13\5\3\5\3\5\6\5")
        buf.write("\u0084\n\5\r\5\16\5\u0085\7\5\u0088\n\5\f\5\16\5\u008b")
        buf.write("\13\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0094\n\5\5\5\u0096")
        buf.write("\n\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\5\n\u00aa\n\n\3\13\3\13\7\13\u00ae")
        buf.write("\n\13\f\13\16\13\u00b1\13\13\3\13\3\13\6\13\u00b5\n\13")
        buf.write("\r\13\16\13\u00b6\7\13\u00b9\n\13\f\13\16\13\u00bc\13")
        buf.write("\13\3\13\5\13\u00bf\n\13\3\f\3\f\7\f\u00c3\n\f\f\f\16")
        buf.write("\f\u00c6\13\f\3\r\3\r\5\r\u00ca\n\r\3\r\6\r\u00cd\n\r")
        buf.write("\r\r\16\r\u00ce\3\16\6\16\u00d2\n\16\r\16\16\16\u00d3")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\2\2\22\3\3\5")
        buf.write("\4\7\5\t\6\13\2\r\2\17\2\21\2\23\7\25\2\27\2\31\2\33\b")
        buf.write("\35\t\37\n!\13\3\2\f\3\2\63;\4\2\63;CH\3\2\639\3\2\62")
        buf.write(";\4\2\62;CH\3\2\629\3\2\62\63\4\2GGgg\4\2--//\5\2\13\f")
        buf.write("\17\17\"\"\2\u00f3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\23\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\3\67\3\2\2\2\5Z\3\2\2\2\7r\3\2")
        buf.write("\2\2\t\u0095\3\2\2\2\13\u0097\3\2\2\2\r\u0099\3\2\2\2")
        buf.write("\17\u009b\3\2\2\2\21\u009d\3\2\2\2\23\u00a9\3\2\2\2\25")
        buf.write("\u00be\3\2\2\2\27\u00c0\3\2\2\2\31\u00c7\3\2\2\2\33\u00d1")
        buf.write("\3\2\2\2\35\u00d7\3\2\2\2\37\u00d9\3\2\2\2!\u00db\3\2")
        buf.write("\2\2#\'\t\2\2\2$&\5\13\6\2%$\3\2\2\2&)\3\2\2\2\'%\3\2")
        buf.write("\2\2\'(\3\2\2\2(\62\3\2\2\2)\'\3\2\2\2*,\7a\2\2+-\5\13")
        buf.write("\6\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\61\3\2\2")
        buf.write("\2\60*\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\65\3\2\2\2\64\62\3\2\2\2\658\b\2\2\2\668\7\62\2")
        buf.write("\2\67#\3\2\2\2\67\66\3\2\2\28\4\3\2\2\29:\7\62\2\2:>\7")
        buf.write("z\2\2;<\7\62\2\2<>\7Z\2\2=9\3\2\2\2=;\3\2\2\2>?\3\2\2")
        buf.write("\2?C\t\3\2\2@B\5\r\7\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2C")
        buf.write("D\3\2\2\2DN\3\2\2\2EC\3\2\2\2FH\7a\2\2GI\5\r\7\2HG\3\2")
        buf.write("\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KM\3\2\2\2LF\3\2\2\2")
        buf.write("MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PN\3\2\2\2Q[\b")
        buf.write("\3\3\2RS\7\62\2\2ST\7z\2\2TY\7\62\2\2UV\7\62\2\2VW\7Z")
        buf.write("\2\2WY\7\62\2\2XR\3\2\2\2XU\3\2\2\2Y[\3\2\2\2Z=\3\2\2")
        buf.write("\2ZX\3\2\2\2[\6\3\2\2\2\\]\7\62\2\2]a\t\4\2\2^`\5\17\b")
        buf.write("\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bl\3\2\2\2c")
        buf.write("a\3\2\2\2df\7a\2\2eg\5\17\b\2fe\3\2\2\2gh\3\2\2\2hf\3")
        buf.write("\2\2\2hi\3\2\2\2ik\3\2\2\2jd\3\2\2\2kn\3\2\2\2lj\3\2\2")
        buf.write("\2lm\3\2\2\2mo\3\2\2\2nl\3\2\2\2os\b\4\4\2pq\7\62\2\2")
        buf.write("qs\7\62\2\2r\\\3\2\2\2rp\3\2\2\2s\b\3\2\2\2tu\7\62\2\2")
        buf.write("uy\7d\2\2vw\7\62\2\2wy\7D\2\2xt\3\2\2\2xv\3\2\2\2yz\3")
        buf.write("\2\2\2z~\7\63\2\2{}\5\21\t\2|{\3\2\2\2}\u0080\3\2\2\2")
        buf.write("~|\3\2\2\2~\177\3\2\2\2\177\u0089\3\2\2\2\u0080~\3\2\2")
        buf.write("\2\u0081\u0083\7a\2\2\u0082\u0084\5\21\t\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0088\3\2\2\2\u0087\u0081\3\2\2\2")
        buf.write("\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3")
        buf.write("\2\2\2\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u0096")
        buf.write("\b\5\5\2\u008d\u008e\7\62\2\2\u008e\u008f\7d\2\2\u008f")
        buf.write("\u0094\7\62\2\2\u0090\u0091\7\62\2\2\u0091\u0092\7D\2")
        buf.write("\2\u0092\u0094\7\62\2\2\u0093\u008d\3\2\2\2\u0093\u0090")
        buf.write("\3\2\2\2\u0094\u0096\3\2\2\2\u0095x\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0096\n\3\2\2\2\u0097\u0098\t\5\2\2\u0098\f\3")
        buf.write("\2\2\2\u0099\u009a\t\6\2\2\u009a\16\3\2\2\2\u009b\u009c")
        buf.write("\t\7\2\2\u009c\20\3\2\2\2\u009d\u009e\t\b\2\2\u009e\22")
        buf.write("\3\2\2\2\u009f\u00a0\5\25\13\2\u00a0\u00a1\5\27\f\2\u00a1")
        buf.write("\u00aa\3\2\2\2\u00a2\u00a3\5\25\13\2\u00a3\u00a4\5\31")
        buf.write("\r\2\u00a4\u00aa\3\2\2\2\u00a5\u00a6\5\25\13\2\u00a6\u00a7")
        buf.write("\5\27\f\2\u00a7\u00a8\5\31\r\2\u00a8\u00aa\3\2\2\2\u00a9")
        buf.write("\u009f\3\2\2\2\u00a9\u00a2\3\2\2\2\u00a9\u00a5\3\2\2\2")
        buf.write("\u00aa\24\3\2\2\2\u00ab\u00af\t\2\2\2\u00ac\u00ae\5\13")
        buf.write("\6\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ba\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b2\u00b4\7a\2\2\u00b3\u00b5\5\13\6\2")
        buf.write("\u00b4\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3")
        buf.write("\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b2")
        buf.write("\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bf\3\2\2\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bd\u00bf\7\62\2\2\u00be\u00ab\3\2\2\2\u00be\u00bd")
        buf.write("\3\2\2\2\u00bf\26\3\2\2\2\u00c0\u00c4\7\60\2\2\u00c1\u00c3")
        buf.write("\5\13\6\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\30\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c9\t\t\2\2\u00c8\u00ca\t\n\2\2")
        buf.write("\u00c9\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3")
        buf.write("\2\2\2\u00cb\u00cd\5\13\6\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\32\3\2\2\2\u00d0\u00d2\t\13\2\2\u00d1\u00d0\3\2")
        buf.write("\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\b\16\6\2\u00d6")
        buf.write("\34\3\2\2\2\u00d7\u00d8\13\2\2\2\u00d8\36\3\2\2\2\u00d9")
        buf.write("\u00da\13\2\2\2\u00da \3\2\2\2\u00db\u00dc\13\2\2\2\u00dc")
        buf.write("\"\3\2\2\2 \2\'.\62\67=CJNXZahlrx~\u0085\u0089\u0093\u0095")
        buf.write("\u00a9\u00af\u00b6\u00ba\u00be\u00c4\u00c9\u00ce\u00d3")
        buf.write("\7\3\2\2\3\3\3\3\4\4\3\5\5\b\2\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER_LITERAL_X10 = 1
    INTEGER_LITERAL_X16 = 2
    INTEGER_LITERAL_X8 = 3
    INTEGER_LITERAL_X2 = 4
    FLOAT_LITERAL = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", "INTEGER_LITERAL_X8", 
            "INTEGER_LITERAL_X2", "FLOAT_LITERAL", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", "INTEGER_LITERAL_X8", 
                  "INTEGER_LITERAL_X2", "NUMBERDIGIT", "X16DIGIT", "X8DIGIT", 
                  "X2DIGIT", "FLOAT_LITERAL", "FLOAT_INT_COMPO", "FLOAT_DECIMAL_COMPO", 
                  "FLOAT_EXPO_COMPO", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
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
     


