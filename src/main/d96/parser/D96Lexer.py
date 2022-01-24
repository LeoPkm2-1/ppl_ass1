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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("\u008d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\3\2\3\2\3\3\3\3\7\3\"\n\3\f\3\16\3%\13\3\3")
        buf.write("\3\3\3\6\3)\n\3\r\3\16\3*\7\3-\n\3\f\3\16\3\60\13\3\3")
        buf.write("\3\3\3\5\3\64\n\3\3\4\3\4\3\4\3\4\5\4:\n\4\3\4\6\4=\n")
        buf.write("\4\r\4\16\4>\3\4\3\4\6\4C\n\4\r\4\16\4D\7\4G\n\4\f\4\16")
        buf.write("\4J\13\4\3\4\3\4\3\5\3\5\6\5P\n\5\r\5\16\5Q\3\5\3\5\6")
        buf.write("\5V\n\5\r\5\16\5W\7\5Z\n\5\f\5\16\5]\13\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\5\6e\n\6\3\6\6\6h\n\6\r\6\16\6i\3\6\3\6\6")
        buf.write("\6n\n\6\r\6\16\6o\7\6r\n\6\f\6\16\6u\13\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13\u0082\n\13\r\13")
        buf.write("\16\13\u0083\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\2\2\17")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\2\17\2\21\2\23\2\25\b\27\t\31")
        buf.write("\n\33\13\3\2\b\3\2\63;\3\2\62;\4\2\62;CH\3\2\629\3\2\62")
        buf.write("\63\5\2\13\f\17\17\"\"\2\u0098\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\63\3")
        buf.write("\2\2\2\79\3\2\2\2\tM\3\2\2\2\13d\3\2\2\2\rx\3\2\2\2\17")
        buf.write("z\3\2\2\2\21|\3\2\2\2\23~\3\2\2\2\25\u0081\3\2\2\2\27")
        buf.write("\u0087\3\2\2\2\31\u0089\3\2\2\2\33\u008b\3\2\2\2\35\36")
        buf.write("\7c\2\2\36\4\3\2\2\2\37#\t\2\2\2 \"\5\r\7\2! \3\2\2\2")
        buf.write("\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$.\3\2\2\2%#\3\2\2\2&(")
        buf.write("\7a\2\2\')\5\r\7\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3")
        buf.write("\2\2\2+-\3\2\2\2,&\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2")
        buf.write("\2\2/\61\3\2\2\2\60.\3\2\2\2\61\64\b\3\2\2\62\64\7\62")
        buf.write("\2\2\63\37\3\2\2\2\63\62\3\2\2\2\64\6\3\2\2\2\65\66\7")
        buf.write("\62\2\2\66:\7z\2\2\678\7\62\2\28:\7Z\2\29\65\3\2\2\29")
        buf.write("\67\3\2\2\2:<\3\2\2\2;=\5\17\b\2<;\3\2\2\2=>\3\2\2\2>")
        buf.write("<\3\2\2\2>?\3\2\2\2?H\3\2\2\2@B\7a\2\2AC\5\17\b\2BA\3")
        buf.write("\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2F@\3\2\2")
        buf.write("\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2IK\3\2\2\2JH\3\2\2\2K")
        buf.write("L\b\4\3\2L\b\3\2\2\2MO\7\62\2\2NP\5\21\t\2ON\3\2\2\2P")
        buf.write("Q\3\2\2\2QO\3\2\2\2QR\3\2\2\2R[\3\2\2\2SU\7a\2\2TV\5\21")
        buf.write("\t\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2")
        buf.write("YS\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2]")
        buf.write("[\3\2\2\2^_\b\5\4\2_\n\3\2\2\2`a\7\62\2\2ae\7d\2\2bc\7")
        buf.write("\62\2\2ce\7D\2\2d`\3\2\2\2db\3\2\2\2eg\3\2\2\2fh\5\23")
        buf.write("\n\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2js\3\2\2\2")
        buf.write("km\7a\2\2ln\5\23\n\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3")
        buf.write("\2\2\2pr\3\2\2\2qk\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2")
        buf.write("\2tv\3\2\2\2us\3\2\2\2vw\b\6\5\2w\f\3\2\2\2xy\t\3\2\2")
        buf.write("y\16\3\2\2\2z{\t\4\2\2{\20\3\2\2\2|}\t\5\2\2}\22\3\2\2")
        buf.write("\2~\177\t\6\2\2\177\24\3\2\2\2\u0080\u0082\t\7\2\2\u0081")
        buf.write("\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0081\3\2\2\2")
        buf.write("\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\b")
        buf.write("\13\6\2\u0086\26\3\2\2\2\u0087\u0088\13\2\2\2\u0088\30")
        buf.write("\3\2\2\2\u0089\u008a\13\2\2\2\u008a\32\3\2\2\2\u008b\u008c")
        buf.write("\13\2\2\2\u008c\34\3\2\2\2\23\2#*.\639>DHQW[dios\u0083")
        buf.write("\7\3\3\2\3\4\3\3\5\4\3\6\5\b\2\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTEGER_LITERAL_X10 = 2
    INTEGER_LITERAL_X16 = 3
    INTEGER_LITERAL_X8 = 4
    INTEGER_LITERAL_X2 = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'a'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", "INTEGER_LITERAL_X8", 
            "INTEGER_LITERAL_X2", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", 
                  "INTEGER_LITERAL_X8", "INTEGER_LITERAL_X2", "NUMBERDIGIT", 
                  "X16DIGIT", "X8DIGIT", "X2DIGIT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
     


