# Generated from e:\UserD\Documents\studying\PPL\ASS\ass1\initial\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\62\n\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6=\n\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\n\3\n\5\nI\n\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13Q\n\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\5\17\\\n\17\3\20\3\20\3\20\5\20a\n\20\3\20")
        buf.write("\2\2\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\3\4\2")
        buf.write("\t\n\f\f\2Y\2 \3\2\2\2\4$\3\2\2\2\6\61\3\2\2\2\b\63\3")
        buf.write("\2\2\2\n<\3\2\2\2\f>\3\2\2\2\16A\3\2\2\2\20D\3\2\2\2\22")
        buf.write("H\3\2\2\2\24P\3\2\2\2\26R\3\2\2\2\30T\3\2\2\2\32V\3\2")
        buf.write("\2\2\34[\3\2\2\2\36`\3\2\2\2 !\5\6\4\2!\"\5\4\3\2\"#\7")
        buf.write("\2\2\3#\3\3\2\2\2$%\5\30\r\2%&\5\26\f\2&\'\7\3\2\2\'(")
        buf.write("\7\17\2\2()\7\20\2\2)*\7\r\2\2*+\7\4\2\2+,\7\16\2\2,\5")
        buf.write("\3\2\2\2-.\5\b\5\2./\5\6\4\2/\62\3\2\2\2\60\62\5\b\5\2")
        buf.write("\61-\3\2\2\2\61\60\3\2\2\2\62\7\3\2\2\2\63\64\5\30\r\2")
        buf.write("\64\65\5\32\16\2\65\66\5\n\6\2\66\67\7\r\2\2\678\7\5\2")
        buf.write("\289\7\16\2\29\t\3\2\2\2:=\5\f\7\2;=\3\2\2\2<:\3\2\2\2")
        buf.write("<;\3\2\2\2=\13\3\2\2\2>?\7\23\2\2?@\5\16\b\2@\r\3\2\2")
        buf.write("\2AB\5\20\t\2BC\5\22\n\2C\17\3\2\2\2DE\5\32\16\2E\21\3")
        buf.write("\2\2\2FI\5\24\13\2GI\3\2\2\2HF\3\2\2\2HG\3\2\2\2I\23\3")
        buf.write("\2\2\2JK\7\22\2\2KL\5\20\t\2LM\5\24\13\2MQ\3\2\2\2NO\7")
        buf.write("\22\2\2OQ\5\20\t\2PJ\3\2\2\2PN\3\2\2\2Q\25\3\2\2\2RS\7")
        buf.write("\6\2\2S\27\3\2\2\2TU\7\7\2\2U\31\3\2\2\2VW\7\b\2\2WX\5")
        buf.write("\34\17\2X\33\3\2\2\2Y\\\5\36\20\2Z\\\3\2\2\2[Y\3\2\2\2")
        buf.write("[Z\3\2\2\2\\\35\3\2\2\2]^\t\2\2\2^a\5\36\20\2_a\t\2\2")
        buf.write("\2`]\3\2\2\2`_\3\2\2\2a\37\3\2\2\2\b\61<HP[`")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'programclassbody'", "'classbody'", 
                     "'Program'", "'Class'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'_'", "'{'", "'}'", "'('", "')'", "';'", 
                     "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "CHAR_SEQ", "CHAR", "NUM", 
                      "NUM_SEQ", "UNDERCORE", "LB", "RB", "LP", "RP", "SM", 
                      "CM", "COLON", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_programclass = 1
    RULE_classdecls = 2
    RULE_classdecl = 3
    RULE_superclasslist = 4
    RULE_parentlist = 5
    RULE_parentlst = 6
    RULE_parent1 = 7
    RULE_otherparents = 8
    RULE_otherparent = 9
    RULE_programkey = 10
    RULE_classkey = 11
    RULE_identifier = 12
    RULE_tail_identifier = 13
    RULE_tailiden = 14

    ruleNames =  [ "program", "programclass", "classdecls", "classdecl", 
                   "superclasslist", "parentlist", "parentlst", "parent1", 
                   "otherparents", "otherparent", "programkey", "classkey", 
                   "identifier", "tail_identifier", "tailiden" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    CHAR_SEQ=6
    CHAR=7
    NUM=8
    NUM_SEQ=9
    UNDERCORE=10
    LB=11
    RB=12
    LP=13
    RP=14
    SM=15
    CM=16
    COLON=17
    WS=18
    ERROR_CHAR=19
    UNCLOSE_STRING=20
    ILLEGAL_ESCAPE=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def programclass(self):
            return self.getTypedRuleContext(D96Parser.ProgramclassContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.classdecls()
            self.state = 31
            self.programclass()
            self.state = 32
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramclassContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classkey(self):
            return self.getTypedRuleContext(D96Parser.ClasskeyContext,0)


        def programkey(self):
            return self.getTypedRuleContext(D96Parser.ProgramkeyContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_programclass




    def programclass(self):

        localctx = D96Parser.ProgramclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programclass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.classkey()
            self.state = 35
            self.programkey()
            self.state = 36
            self.match(D96Parser.T__0)
            self.state = 37
            self.match(D96Parser.LP)
            self.state = 38
            self.match(D96Parser.RP)
            self.state = 39
            self.match(D96Parser.LB)
            self.state = 40
            self.match(D96Parser.T__1)
            self.state = 41
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclContext,0)


        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecls




    def classdecls(self):

        localctx = D96Parser.ClassdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecls)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.classdecl()
                self.state = 44
                self.classdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.classdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classkey(self):
            return self.getTypedRuleContext(D96Parser.ClasskeyContext,0)


        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def superclasslist(self):
            return self.getTypedRuleContext(D96Parser.SuperclasslistContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classdecl




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.classkey()
            self.state = 50
            self.identifier()
            self.state = 51
            self.superclasslist()
            self.state = 52
            self.match(D96Parser.LB)
            self.state = 53
            self.match(D96Parser.T__2)
            self.state = 54
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperclasslistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parentlist(self):
            return self.getTypedRuleContext(D96Parser.ParentlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_superclasslist




    def superclasslist(self):

        localctx = D96Parser.SuperclasslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_superclasslist)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.parentlist()
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParentlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def parentlst(self):
            return self.getTypedRuleContext(D96Parser.ParentlstContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parentlist




    def parentlist(self):

        localctx = D96Parser.ParentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parentlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(D96Parser.COLON)
            self.state = 61
            self.parentlst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParentlstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parent1(self):
            return self.getTypedRuleContext(D96Parser.Parent1Context,0)


        def otherparents(self):
            return self.getTypedRuleContext(D96Parser.OtherparentsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parentlst




    def parentlst(self):

        localctx = D96Parser.ParentlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parentlst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.parent1()
            self.state = 64
            self.otherparents()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parent1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parent1




    def parent1(self):

        localctx = D96Parser.Parent1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parent1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherparentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def otherparent(self):
            return self.getTypedRuleContext(D96Parser.OtherparentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_otherparents




    def otherparents(self):

        localctx = D96Parser.OtherparentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_otherparents)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.otherparent()
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherparentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def parent1(self):
            return self.getTypedRuleContext(D96Parser.Parent1Context,0)


        def otherparent(self):
            return self.getTypedRuleContext(D96Parser.OtherparentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_otherparent




    def otherparent(self):

        localctx = D96Parser.OtherparentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_otherparent)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(D96Parser.CM)
                self.state = 73
                self.parent1()
                self.state = 74
                self.otherparent()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(D96Parser.CM)
                self.state = 77
                self.parent1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramkeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_programkey




    def programkey(self):

        localctx = D96Parser.ProgramkeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_programkey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(D96Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClasskeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_classkey




    def classkey(self):

        localctx = D96Parser.ClasskeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_classkey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(D96Parser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR_SEQ(self):
            return self.getToken(D96Parser.CHAR_SEQ, 0)

        def tail_identifier(self):
            return self.getTypedRuleContext(D96Parser.Tail_identifierContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_identifier




    def identifier(self):

        localctx = D96Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(D96Parser.CHAR_SEQ)
            self.state = 85
            self.tail_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tail_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tailiden(self):
            return self.getTypedRuleContext(D96Parser.TailidenContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_tail_identifier




    def tail_identifier(self):

        localctx = D96Parser.Tail_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_tail_identifier)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CHAR, D96Parser.NUM, D96Parser.UNDERCORE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.tailiden()
                pass
            elif token in [D96Parser.LB, D96Parser.CM, D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TailidenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tailiden(self):
            return self.getTypedRuleContext(D96Parser.TailidenContext,0)


        def CHAR(self):
            return self.getToken(D96Parser.CHAR, 0)

        def NUM(self):
            return self.getToken(D96Parser.NUM, 0)

        def UNDERCORE(self):
            return self.getToken(D96Parser.UNDERCORE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_tailiden




    def tailiden(self):

        localctx = D96Parser.TailidenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_tailiden)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CHAR) | (1 << D96Parser.NUM) | (1 << D96Parser.UNDERCORE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 92
                self.tailiden()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CHAR) | (1 << D96Parser.NUM) | (1 << D96Parser.UNDERCORE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





