# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecls.
    def visitClassdecls(self, ctx:D96Parser.ClassdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecl.
    def visitClassdecl(self, ctx:D96Parser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parentclassname.
    def visitParentclassname(self, ctx:D96Parser.ParentclassnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classbody.
    def visitClassbody(self, ctx:D96Parser.ClassbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classelements.
    def visitClasselements(self, ctx:D96Parser.ClasselementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classelement.
    def visitClasselement(self, ctx:D96Parser.ClasselementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributedecl.
    def visitAttributedecl(self, ctx:D96Parser.AttributedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_key_decl.
    def visitAttribute_key_decl(self, ctx:D96Parser.Attribute_key_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_list.
    def visitVar_list(self, ctx:D96Parser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_typ.
    def visitVar_typ(self, ctx:D96Parser.Var_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_value.
    def visitList_of_value(self, ctx:D96Parser.List_of_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#integer_literal.
    def visitInteger_literal(self, ctx:D96Parser.Integer_literalContext):
        return self.visitChildren(ctx)



del D96Parser