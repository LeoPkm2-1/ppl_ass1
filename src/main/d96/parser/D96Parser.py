# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\f\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\2\2\4\2\4\2")
        buf.write("\2\2\t\2\6\3\2\2\2\4\t\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3")
        buf.write("\b\3\3\2\2\2\t\n\7\3\2\2\n\5\3\2\2\2\2")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", 
                      "INTEGER_LITERAL_X8", "INTEGER_LITERAL_X2", "FLOAT_LITERAL", 
                      "BOOLEAN_LITERAL", "STRING_LITERAL", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecls = 1

    ruleNames =  [ "program", "classdecls" ]

    EOF = Token.EOF
    INTEGER_LITERAL_X10=1
    INTEGER_LITERAL_X16=2
    INTEGER_LITERAL_X8=3
    INTEGER_LITERAL_X2=4
    FLOAT_LITERAL=5
    BOOLEAN_LITERAL=6
    STRING_LITERAL=7
    WS=8
    ERROR_CHAR=9
    UNCLOSE_STRING=10
    ILLEGAL_ESCAPE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.classdecls()
            self.state = 5
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL_X10(self):
            return self.getToken(D96Parser.INTEGER_LITERAL_X10, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classdecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecls" ):
                return visitor.visitClassdecls(self)
            else:
                return visitor.visitChildren(self)




    def classdecls(self):

        localctx = D96Parser.ClassdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(D96Parser.INTEGER_LITERAL_X10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





