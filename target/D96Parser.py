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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3(\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\64")
        buf.write("\n\5\3\6\3\6\5\68\n\6\3\7\3\7\3\7\3\7\5\7>\n\7\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5\nK\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13R\n\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\5\17`\n\17\3\20\3\20\3\20")
        buf.write("\2\2\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\6\3\2")
        buf.write("\24\25\4\2\32\32\34\34\3\2\26\31\3\2\4\7\2^\2 \3\2\2\2")
        buf.write("\4\'\3\2\2\2\6)\3\2\2\2\b\63\3\2\2\2\n\67\3\2\2\2\f=\3")
        buf.write("\2\2\2\16?\3\2\2\2\20A\3\2\2\2\22J\3\2\2\2\24Q\3\2\2\2")
        buf.write("\26S\3\2\2\2\30U\3\2\2\2\32W\3\2\2\2\34_\3\2\2\2\36a\3")
        buf.write("\2\2\2 !\5\4\3\2!\"\7\2\2\3\"\3\3\2\2\2#$\5\6\4\2$%\5")
        buf.write("\4\3\2%(\3\2\2\2&(\5\6\4\2\'#\3\2\2\2\'&\3\2\2\2(\5\3")
        buf.write("\2\2\2)*\7\f\2\2*+\7\33\2\2+,\5\b\5\2,-\7\17\2\2-.\5\n")
        buf.write("\6\2./\7\20\2\2/\7\3\2\2\2\60\61\7\23\2\2\61\64\7\33\2")
        buf.write("\2\62\64\3\2\2\2\63\60\3\2\2\2\63\62\3\2\2\2\64\t\3\2")
        buf.write("\2\2\658\5\f\7\2\668\3\2\2\2\67\65\3\2\2\2\67\66\3\2\2")
        buf.write("\28\13\3\2\2\29:\5\16\b\2:;\5\f\7\2;>\3\2\2\2<>\5\16\b")
        buf.write("\2=9\3\2\2\2=<\3\2\2\2>\r\3\2\2\2?@\5\20\t\2@\17\3\2\2")
        buf.write("\2AB\t\2\2\2BC\5\24\13\2CD\7\23\2\2DE\5\30\r\2EF\5\22")
        buf.write("\n\2FG\7\21\2\2G\21\3\2\2\2HK\5\32\16\2IK\3\2\2\2JH\3")
        buf.write("\2\2\2JI\3\2\2\2K\23\3\2\2\2LM\5\26\f\2MN\7\22\2\2NO\5")
        buf.write("\24\13\2OR\3\2\2\2PR\5\26\f\2QL\3\2\2\2QP\3\2\2\2R\25")
        buf.write("\3\2\2\2ST\t\3\2\2T\27\3\2\2\2UV\t\4\2\2V\31\3\2\2\2W")
        buf.write("X\7\3\2\2XY\5\34\17\2Y\33\3\2\2\2Z`\3\2\2\2[`\5\36\20")
        buf.write("\2\\`\7\b\2\2]`\7\t\2\2^`\7\n\2\2_Z\3\2\2\2_[\3\2\2\2")
        buf.write("_\\\3\2\2\2_]\3\2\2\2_^\3\2\2\2`\35\3\2\2\2ab\t\5\2\2")
        buf.write("b\37\3\2\2\2\t\'\63\67=JQ_")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Array'", "'Class'", "'('", "')'", "'{'", "'}'", "';'", 
                     "','", "':'", "'Val'", "'Var'", "'Boolean'", "'Int'", 
                     "'Float'", "'String'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTEGER_LITERAL_X10", "INTEGER_LITERAL_X16", 
                      "INTEGER_LITERAL_X8", "INTEGER_LITERAL_X2", "FLOAT_LITERAL", 
                      "BOOLEAN_LITERAL", "STRING_LITERAL", "Array", "CLASS", 
                      "LP", "RP", "LB", "RB", "SM", "CM", "COLON", "VAL", 
                      "VAR", "BOOLEAN_TYP", "INT_TYP", "FLOAT_TYP", "STRING_TYP", 
                      "IDENTIFIER", "CLASSNAME", "STATIC_IDENTIFIER", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecls = 1
    RULE_classdecl = 2
    RULE_parentclassname = 3
    RULE_classbody = 4
    RULE_classelements = 5
    RULE_classelement = 6
    RULE_attributedecl = 7
    RULE_values = 8
    RULE_varlist = 9
    RULE_var_item = 10
    RULE_typ = 11
    RULE_valus = 12
    RULE_list_of_value = 13
    RULE_integer_literal = 14

    ruleNames =  [ "program", "classdecls", "classdecl", "parentclassname", 
                   "classbody", "classelements", "classelement", "attributedecl", 
                   "values", "varlist", "var_item", "typ", "valus", "list_of_value", 
                   "integer_literal" ]

    EOF = Token.EOF
    T__0=1
    INTEGER_LITERAL_X10=2
    INTEGER_LITERAL_X16=3
    INTEGER_LITERAL_X8=4
    INTEGER_LITERAL_X2=5
    FLOAT_LITERAL=6
    BOOLEAN_LITERAL=7
    STRING_LITERAL=8
    Array=9
    CLASS=10
    LP=11
    RP=12
    LB=13
    RB=14
    SM=15
    CM=16
    COLON=17
    VAL=18
    VAR=19
    BOOLEAN_TYP=20
    INT_TYP=21
    FLOAT_TYP=22
    STRING_TYP=23
    IDENTIFIER=24
    CLASSNAME=25
    STATIC_IDENTIFIER=26
    WS=27
    UNCLOSE_STRING=28
    ILLEGAL_ESCAPE=29
    ERROR_CHAR=30

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
            self.state = 30
            self.classdecls()
            self.state = 31
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
        self.enterRule(localctx, 2, self.RULE_classdecls)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.classdecl()
                self.state = 34
                self.classdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
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

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def CLASSNAME(self):
            return self.getToken(D96Parser.CLASSNAME, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(D96Parser.CLASS)
            self.state = 40
            self.match(D96Parser.CLASSNAME)
            self.state = 41
            self.parentclassname()
            self.state = 42
            self.match(D96Parser.LB)
            self.state = 43
            self.classbody()
            self.state = 44
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParentclassnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def CLASSNAME(self):
            return self.getToken(D96Parser.CLASSNAME, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_parentclassname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentclassname" ):
                return visitor.visitParentclassname(self)
            else:
                return visitor.visitChildren(self)




    def parentclassname(self):

        localctx = D96Parser.ParentclassnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parentclassname)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(D96Parser.COLON)
                self.state = 47
                self.match(D96Parser.CLASSNAME)
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classelements(self):
            return self.getTypedRuleContext(D96Parser.ClasselementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassbody" ):
                return visitor.visitClassbody(self)
            else:
                return visitor.visitChildren(self)




    def classbody(self):

        localctx = D96Parser.ClassbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classbody)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classelement(self):
            return self.getTypedRuleContext(D96Parser.ClasselementContext,0)


        def classelements(self):
            return self.getTypedRuleContext(D96Parser.ClasselementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classelements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasselements" ):
                return visitor.visitClasselements(self)
            else:
                return visitor.visitChildren(self)




    def classelements(self):

        localctx = D96Parser.ClasselementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classelements)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.classelement()
                self.state = 56
                self.classelements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributedecl(self):
            return self.getTypedRuleContext(D96Parser.AttributedeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classelement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasselement" ):
                return visitor.visitClasselement(self)
            else:
                return visitor.visitChildren(self)




    def classelement(self):

        localctx = D96Parser.ClasselementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_classelement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.attributedecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varlist(self):
            return self.getTypedRuleContext(D96Parser.VarlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def values(self):
            return self.getTypedRuleContext(D96Parser.ValuesContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = D96Parser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 64
            self.varlist()
            self.state = 65
            self.match(D96Parser.COLON)
            self.state = 66
            self.typ()
            self.state = 67
            self.values()
            self.state = 68
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valus(self):
            return self.getTypedRuleContext(D96Parser.ValusContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_values

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValues" ):
                return visitor.visitValues(self)
            else:
                return visitor.visitChildren(self)




    def values(self):

        localctx = D96Parser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_values)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.valus()
                pass
            elif token in [D96Parser.SM]:
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


    class VarlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_item(self):
            return self.getTypedRuleContext(D96Parser.Var_itemContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def varlist(self):
            return self.getTypedRuleContext(D96Parser.VarlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_varlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist" ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = D96Parser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_varlist)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.var_item()
                self.state = 75
                self.match(D96Parser.CM)
                self.state = 76
                self.varlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.var_item()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def STATIC_IDENTIFIER(self):
            return self.getToken(D96Parser.STATIC_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_item" ):
                return visitor.visitVar_item(self)
            else:
                return visitor.visitChildren(self)




    def var_item(self):

        localctx = D96Parser.Var_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.STATIC_IDENTIFIER):
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


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

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
            return D96Parser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = D96Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
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


    class ValusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_of_value(self):
            return self.getTypedRuleContext(D96Parser.List_of_valueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_valus

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValus" ):
                return visitor.visitValus(self)
            else:
                return visitor.visitChildren(self)




    def valus(self):

        localctx = D96Parser.ValusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_valus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(D96Parser.T__0)
            self.state = 86
            self.list_of_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_valueContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_value" ):
                return visitor.visitList_of_value(self)
            else:
                return visitor.visitChildren(self)




    def list_of_value(self):

        localctx = D96Parser.List_of_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_of_value)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SM]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.INTEGER_LITERAL_X10, D96Parser.INTEGER_LITERAL_X16, D96Parser.INTEGER_LITERAL_X8, D96Parser.INTEGER_LITERAL_X2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.integer_literal()
                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.match(D96Parser.FLOAT_LITERAL)
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger_literal" ):
                return visitor.visitInteger_literal(self)
            else:
                return visitor.visitChildren(self)




    def integer_literal(self):

        localctx = D96Parser.Integer_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_integer_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
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





