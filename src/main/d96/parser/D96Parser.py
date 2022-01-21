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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("l\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\5\5\67\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\5\bD\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\5\fP\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\rX\n\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\5\21c\n\21\3")
        buf.write("\22\3\22\3\22\5\22h\n\22\3\23\3\23\3\23\2\2\24\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$\2\4\4\2\r\16\20\20")
        buf.write("\3\2\7\n\2_\2&\3\2\2\2\4*\3\2\2\2\6\60\3\2\2\2\b\66\3")
        buf.write("\2\2\2\n8\3\2\2\2\f?\3\2\2\2\16C\3\2\2\2\20E\3\2\2\2\22")
        buf.write("H\3\2\2\2\24K\3\2\2\2\26O\3\2\2\2\30W\3\2\2\2\32Y\3\2")
        buf.write("\2\2\34[\3\2\2\2\36]\3\2\2\2 b\3\2\2\2\"g\3\2\2\2$i\3")
        buf.write("\2\2\2&\'\5\b\5\2\'(\5\4\3\2()\7\2\2\3)\3\3\2\2\2*+\5")
        buf.write("\34\17\2+,\5\32\16\2,-\7\21\2\2-.\5\6\4\2./\7\22\2\2/")
        buf.write("\5\3\2\2\2\60\61\7\3\2\2\61\7\3\2\2\2\62\63\5\n\6\2\63")
        buf.write("\64\5\b\5\2\64\67\3\2\2\2\65\67\5\n\6\2\66\62\3\2\2\2")
        buf.write("\66\65\3\2\2\2\67\t\3\2\2\289\5\34\17\29:\5\36\20\2:;")
        buf.write("\5\16\b\2;<\7\21\2\2<=\5\f\7\2=>\7\22\2\2>\13\3\2\2\2")
        buf.write("?@\7\4\2\2@\r\3\2\2\2AD\5\20\t\2BD\3\2\2\2CA\3\2\2\2C")
        buf.write("B\3\2\2\2D\17\3\2\2\2EF\7\27\2\2FG\5\22\n\2G\21\3\2\2")
        buf.write("\2HI\5\24\13\2IJ\5\26\f\2J\23\3\2\2\2KL\5\36\20\2L\25")
        buf.write("\3\2\2\2MP\5\30\r\2NP\3\2\2\2OM\3\2\2\2ON\3\2\2\2P\27")
        buf.write("\3\2\2\2QR\7\26\2\2RS\5\24\13\2ST\5\30\r\2TX\3\2\2\2U")
        buf.write("V\7\26\2\2VX\5\24\13\2WQ\3\2\2\2WU\3\2\2\2X\31\3\2\2\2")
        buf.write("YZ\7\5\2\2Z\33\3\2\2\2[\\\7\6\2\2\\\35\3\2\2\2]^\7\f\2")
        buf.write("\2^_\5 \21\2_\37\3\2\2\2`c\5\"\22\2ac\3\2\2\2b`\3\2\2")
        buf.write("\2ba\3\2\2\2c!\3\2\2\2de\t\2\2\2eh\5\"\22\2fh\t\2\2\2")
        buf.write("gd\3\2\2\2gf\3\2\2\2h#\3\2\2\2ij\t\3\2\2j%\3\2\2\2\b\66")
        buf.write("COWbg")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programclassbody'", "'classbody'", "'Program'", 
                     "'Class'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'_'", "'{'", "'}'", "'('", "')'", "';'", 
                     "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT_DEC", "INT_OCT", "INT_HEX", "INT_BIN", 
                      "FLOAT", "CHAR_SEQ", "CHAR", "NUM", "NUM_SEQ", "UNDERCORE", 
                      "LB", "RB", "LP", "RP", "SM", "CM", "COLON", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_programclass = 1
    RULE_programclassbody = 2
    RULE_classdecls = 3
    RULE_classdecl = 4
    RULE_classbody = 5
    RULE_superclasslist = 6
    RULE_parentlist = 7
    RULE_parentlst = 8
    RULE_parent1 = 9
    RULE_otherparents = 10
    RULE_otherparent = 11
    RULE_programkey = 12
    RULE_classkey = 13
    RULE_identifier = 14
    RULE_tail_identifier = 15
    RULE_tailiden = 16
    RULE_integer = 17

    ruleNames =  [ "program", "programclass", "programclassbody", "classdecls", 
                   "classdecl", "classbody", "superclasslist", "parentlist", 
                   "parentlst", "parent1", "otherparents", "otherparent", 
                   "programkey", "classkey", "identifier", "tail_identifier", 
                   "tailiden", "integer" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    INT_DEC=5
    INT_OCT=6
    INT_HEX=7
    INT_BIN=8
    FLOAT=9
    CHAR_SEQ=10
    CHAR=11
    NUM=12
    NUM_SEQ=13
    UNDERCORE=14
    LB=15
    RB=16
    LP=17
    RP=18
    SM=19
    CM=20
    COLON=21
    WS=22
    ERROR_CHAR=23
    UNCLOSE_STRING=24
    ILLEGAL_ESCAPE=25

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


        def programclass(self):
            return self.getTypedRuleContext(D96Parser.ProgramclassContext,0)


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
            self.state = 36
            self.classdecls()
            self.state = 37
            self.programclass()
            self.state = 38
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classkey(self):
            return self.getTypedRuleContext(D96Parser.ClasskeyContext,0)


        def programkey(self):
            return self.getTypedRuleContext(D96Parser.ProgramkeyContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def programclassbody(self):
            return self.getTypedRuleContext(D96Parser.ProgramclassbodyContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_programclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramclass" ):
                return visitor.visitProgramclass(self)
            else:
                return visitor.visitChildren(self)




    def programclass(self):

        localctx = D96Parser.ProgramclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programclass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.classkey()
            self.state = 41
            self.programkey()
            self.state = 42
            self.match(D96Parser.LB)
            self.state = 43
            self.programclassbody()
            self.state = 44
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramclassbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_programclassbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramclassbody" ):
                return visitor.visitProgramclassbody(self)
            else:
                return visitor.visitChildren(self)




    def programclassbody(self):

        localctx = D96Parser.ProgramclassbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_programclassbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(D96Parser.T__0)
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

        def classdecl(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclContext,0)


        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecls" ):
                return visitor.visitClassdecls(self)
            else:
                return visitor.visitChildren(self)




    def classdecls(self):

        localctx = D96Parser.ClassdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classdecls)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.classdecl()
                self.state = 49
                self.classdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
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
        __slots__ = 'parser'

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

        def classbody(self):
            return self.getTypedRuleContext(D96Parser.ClassbodyContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.classkey()
            self.state = 55
            self.identifier()
            self.state = 56
            self.superclasslist()
            self.state = 57
            self.match(D96Parser.LB)
            self.state = 58
            self.classbody()
            self.state = 59
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_classbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassbody" ):
                return visitor.visitClassbody(self)
            else:
                return visitor.visitChildren(self)




    def classbody(self):

        localctx = D96Parser.ClassbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(D96Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperclasslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parentlist(self):
            return self.getTypedRuleContext(D96Parser.ParentlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_superclasslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperclasslist" ):
                return visitor.visitSuperclasslist(self)
            else:
                return visitor.visitChildren(self)




    def superclasslist(self):

        localctx = D96Parser.SuperclasslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_superclasslist)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def parentlst(self):
            return self.getTypedRuleContext(D96Parser.ParentlstContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parentlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentlist" ):
                return visitor.visitParentlist(self)
            else:
                return visitor.visitChildren(self)




    def parentlist(self):

        localctx = D96Parser.ParentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parentlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(D96Parser.COLON)
            self.state = 68
            self.parentlst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParentlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parent1(self):
            return self.getTypedRuleContext(D96Parser.Parent1Context,0)


        def otherparents(self):
            return self.getTypedRuleContext(D96Parser.OtherparentsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parentlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentlst" ):
                return visitor.visitParentlst(self)
            else:
                return visitor.visitChildren(self)




    def parentlst(self):

        localctx = D96Parser.ParentlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parentlst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.parent1()
            self.state = 71
            self.otherparents()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parent1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parent1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParent1" ):
                return visitor.visitParent1(self)
            else:
                return visitor.visitChildren(self)




    def parent1(self):

        localctx = D96Parser.Parent1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parent1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherparentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def otherparent(self):
            return self.getTypedRuleContext(D96Parser.OtherparentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_otherparents

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherparents" ):
                return visitor.visitOtherparents(self)
            else:
                return visitor.visitChildren(self)




    def otherparents(self):

        localctx = D96Parser.OtherparentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_otherparents)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherparent" ):
                return visitor.visitOtherparent(self)
            else:
                return visitor.visitChildren(self)




    def otherparent(self):

        localctx = D96Parser.OtherparentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_otherparent)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(D96Parser.CM)
                self.state = 80
                self.parent1()
                self.state = 81
                self.otherparent()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(D96Parser.CM)
                self.state = 84
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_programkey

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramkey" ):
                return visitor.visitProgramkey(self)
            else:
                return visitor.visitChildren(self)




    def programkey(self):

        localctx = D96Parser.ProgramkeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_programkey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(D96Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClasskeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_classkey

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasskey" ):
                return visitor.visitClasskey(self)
            else:
                return visitor.visitChildren(self)




    def classkey(self):

        localctx = D96Parser.ClasskeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_classkey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(D96Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR_SEQ(self):
            return self.getToken(D96Parser.CHAR_SEQ, 0)

        def tail_identifier(self):
            return self.getTypedRuleContext(D96Parser.Tail_identifierContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = D96Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(D96Parser.CHAR_SEQ)
            self.state = 92
            self.tail_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tail_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tailiden(self):
            return self.getTypedRuleContext(D96Parser.TailidenContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_tail_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_identifier" ):
                return visitor.visitTail_identifier(self)
            else:
                return visitor.visitChildren(self)




    def tail_identifier(self):

        localctx = D96Parser.Tail_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_tail_identifier)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CHAR, D96Parser.NUM, D96Parser.UNDERCORE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTailiden" ):
                return visitor.visitTailiden(self)
            else:
                return visitor.visitChildren(self)




    def tailiden(self):

        localctx = D96Parser.TailidenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tailiden)
        self._la = 0 # Token type
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CHAR) | (1 << D96Parser.NUM) | (1 << D96Parser.UNDERCORE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 99
                self.tailiden()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
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


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_DEC(self):
            return self.getToken(D96Parser.INT_DEC, 0)

        def INT_OCT(self):
            return self.getToken(D96Parser.INT_OCT, 0)

        def INT_HEX(self):
            return self.getToken(D96Parser.INT_HEX, 0)

        def INT_BIN(self):
            return self.getToken(D96Parser.INT_BIN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_integer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = D96Parser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT_DEC) | (1 << D96Parser.INT_OCT) | (1 << D96Parser.INT_HEX) | (1 << D96Parser.INT_BIN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





