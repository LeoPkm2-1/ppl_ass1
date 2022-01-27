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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\60\n\5\3\6\3\6\5\6\64\n")
        buf.write("\6\3\7\3\7\3\7\3\7\5\7:\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\5\13J\n\13\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\5\rS\n\r\3\16\3\16\3\16\2\2\17\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\2\5\3\2\f\r\3\2\25\30")
        buf.write("\3\2\3\6\2R\2\34\3\2\2\2\4#\3\2\2\2\6%\3\2\2\2\b/\3\2")
        buf.write("\2\2\n\63\3\2\2\2\f9\3\2\2\2\16;\3\2\2\2\20=\3\2\2\2\22")
        buf.write("C\3\2\2\2\24I\3\2\2\2\26K\3\2\2\2\30R\3\2\2\2\32T\3\2")
        buf.write("\2\2\34\35\5\4\3\2\35\36\7\2\2\3\36\3\3\2\2\2\37 \5\6")
        buf.write("\4\2 !\5\4\3\2!$\3\2\2\2\"$\5\6\4\2#\37\3\2\2\2#\"\3\2")
        buf.write("\2\2$\5\3\2\2\2%&\7\n\2\2&\'\7\31\2\2\'(\5\b\5\2()\7\20")
        buf.write("\2\2)*\5\n\6\2*+\7\21\2\2+\7\3\2\2\2,-\7\24\2\2-\60\7")
        buf.write("\31\2\2.\60\3\2\2\2/,\3\2\2\2/.\3\2\2\2\60\t\3\2\2\2\61")
        buf.write("\64\5\f\7\2\62\64\3\2\2\2\63\61\3\2\2\2\63\62\3\2\2\2")
        buf.write("\64\13\3\2\2\2\65\66\5\16\b\2\66\67\5\f\7\2\67:\3\2\2")
        buf.write("\28:\5\16\b\29\65\3\2\2\298\3\2\2\2:\r\3\2\2\2;<\5\20")
        buf.write("\t\2<\17\3\2\2\2=>\5\22\n\2>?\5\24\13\2?@\7\24\2\2@A\5")
        buf.write("\26\f\2AB\7\22\2\2B\21\3\2\2\2CD\t\2\2\2D\23\3\2\2\2E")
        buf.write("F\7\31\2\2FG\7\23\2\2GJ\5\24\13\2HJ\7\31\2\2IE\3\2\2\2")
        buf.write("IH\3\2\2\2J\25\3\2\2\2KL\t\3\2\2L\27\3\2\2\2MS\3\2\2\2")
        buf.write("NS\5\32\16\2OS\7\7\2\2PS\7\b\2\2QS\7\t\2\2RM\3\2\2\2R")
        buf.write("N\3\2\2\2RO\3\2\2\2RP\3\2\2\2RQ\3\2\2\2S\31\3\2\2\2TU")
        buf.write("\t\4\2\2U\33\3\2\2\2\b#/\639IR")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Class'", "'Array'", "'Var'", "'Val'", "'('", "')'", 
                     "'{'", "'}'", "';'", "','", "':'", "'Boolean'", "'Int'", 
                     "'Float'", "'String'" ]

    symbolicNames = [ "<INVALID>", "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", 
                      "INTEGER_LITERAL_X8", "INTEGER_LITERAL_X2", "FLOAT_LITERAL", 
                      "BOOLEAN_LITERAL", "STRING_LITERAL", "CLASS", "Array", 
                      "VAR", "VAL", "LP", "RP", "LB", "RB", "SM", "CM", 
                      "COLON", "BOOLEAN_TYP", "INT_TYP", "FLOAT_TYP", "STRING_TYP", 
                      "IDENTIFIER", "STATIC_IDENTIFIER", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecls = 1
    RULE_classdecl = 2
    RULE_parentclassname = 3
    RULE_classbody = 4
    RULE_classelements = 5
    RULE_classelement = 6
    RULE_attributedecl = 7
    RULE_attribute_key_decl = 8
    RULE_var_list = 9
    RULE_var_typ = 10
    RULE_list_of_value = 11
    RULE_integer_literal = 12

    ruleNames =  [ "program", "classdecls", "classdecl", "parentclassname", 
                   "classbody", "classelements", "classelement", "attributedecl", 
                   "attribute_key_decl", "var_list", "var_typ", "list_of_value", 
                   "integer_literal" ]

    EOF = Token.EOF
    INTEGER_LITERAL_X10=1
    INTEGER_LITERAL_X16=2
    INTEGER_LITERAL_X8=3
    INTEGER_LITERAL_X2=4
    FLOAT_LITERAL=5
    BOOLEAN_LITERAL=6
    STRING_LITERAL=7
    CLASS=8
    Array=9
    VAR=10
    VAL=11
    LP=12
    RP=13
    LB=14
    RB=15
    SM=16
    CM=17
    COLON=18
    BOOLEAN_TYP=19
    INT_TYP=20
    FLOAT_TYP=21
    STRING_TYP=22
    IDENTIFIER=23
    STATIC_IDENTIFIER=24
    WS=25
    UNCLOSE_STRING=26
    ILLEGAL_ESCAPE=27
    ERROR_CHAR=28

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


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.classdecls()
            self.state = 27
            self.match(D96Parser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_classdecls)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.classdecl()
                self.state = 30
                self.classdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
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

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def parentclassname(self):
            return self.getTypedRuleContext(D96Parser.ParentclassnameContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def classbody(self):
            return self.getTypedRuleContext(D96Parser.ClassbodyContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classdecl




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(D96Parser.CLASS)
            self.state = 36
            self.match(D96Parser.IDENTIFIER)
            self.state = 37
            self.parentclassname()
            self.state = 38
            self.match(D96Parser.LB)
            self.state = 39
            self.classbody()
            self.state = 40
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParentclassnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_parentclassname




    def parentclassname(self):

        localctx = D96Parser.ParentclassnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parentclassname)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(D96Parser.COLON)
                self.state = 43
                self.match(D96Parser.IDENTIFIER)
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


    class ClassbodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classelements(self):
            return self.getTypedRuleContext(D96Parser.ClasselementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classbody




    def classbody(self):

        localctx = D96Parser.ClassbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classbody)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR, D96Parser.VAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.classelements()
                pass
            elif token in [D96Parser.RB]:
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


    class ClasselementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classelement(self):
            return self.getTypedRuleContext(D96Parser.ClasselementContext,0)


        def classelements(self):
            return self.getTypedRuleContext(D96Parser.ClasselementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classelements




    def classelements(self):

        localctx = D96Parser.ClasselementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classelements)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.classelement()
                self.state = 52
                self.classelements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.classelement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClasselementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributedecl(self):
            return self.getTypedRuleContext(D96Parser.AttributedeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classelement




    def classelement(self):

        localctx = D96Parser.ClasselementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_classelement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.attributedecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributedeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_key_decl(self):
            return self.getTypedRuleContext(D96Parser.Attribute_key_declContext,0)


        def var_list(self):
            return self.getTypedRuleContext(D96Parser.Var_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def var_typ(self):
            return self.getTypedRuleContext(D96Parser.Var_typContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attributedecl




    def attributedecl(self):

        localctx = D96Parser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.attribute_key_decl()
            self.state = 60
            self.var_list()
            self.state = 61
            self.match(D96Parser.COLON)
            self.state = 62
            self.var_typ()
            self.state = 63
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_key_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_key_decl




    def attribute_key_decl(self):

        localctx = D96Parser.Attribute_key_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_key_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
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


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def var_list(self):
            return self.getTypedRuleContext(D96Parser.Var_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_list




    def var_list(self):

        localctx = D96Parser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_list)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(D96Parser.IDENTIFIER)
                self.state = 68
                self.match(D96Parser.CM)
                self.state = 69
                self.var_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(D96Parser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN_TYP(self):
            return self.getToken(D96Parser.BOOLEAN_TYP, 0)

        def INT_TYP(self):
            return self.getToken(D96Parser.INT_TYP, 0)

        def FLOAT_TYP(self):
            return self.getToken(D96Parser.FLOAT_TYP, 0)

        def STRING_TYP(self):
            return self.getToken(D96Parser.STRING_TYP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_typ




    def var_typ(self):

        localctx = D96Parser.Var_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_TYP) | (1 << D96Parser.INT_TYP) | (1 << D96Parser.FLOAT_TYP) | (1 << D96Parser.STRING_TYP))) != 0)):
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


    class List_of_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer_literal(self):
            return self.getTypedRuleContext(D96Parser.Integer_literalContext,0)


        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_list_of_value




    def list_of_value(self):

        localctx = D96Parser.List_of_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_of_value)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.INTEGER_LITERAL_X10, D96Parser.INTEGER_LITERAL_X16, D96Parser.INTEGER_LITERAL_X8, D96Parser.INTEGER_LITERAL_X2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.integer_literal()
                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.match(D96Parser.FLOAT_LITERAL)
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.match(D96Parser.STRING_LITERAL)
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


    class Integer_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL_X10(self):
            return self.getToken(D96Parser.INTEGER_LITERAL_X10, 0)

        def INTEGER_LITERAL_X16(self):
            return self.getToken(D96Parser.INTEGER_LITERAL_X16, 0)

        def INTEGER_LITERAL_X8(self):
            return self.getToken(D96Parser.INTEGER_LITERAL_X8, 0)

        def INTEGER_LITERAL_X2(self):
            return self.getToken(D96Parser.INTEGER_LITERAL_X2, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_integer_literal




    def integer_literal(self):

        localctx = D96Parser.Integer_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_integer_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER_LITERAL_X10) | (1 << D96Parser.INTEGER_LITERAL_X16) | (1 << D96Parser.INTEGER_LITERAL_X8) | (1 << D96Parser.INTEGER_LITERAL_X2))) != 0)):
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





