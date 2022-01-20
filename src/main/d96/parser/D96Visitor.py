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


    # Visit a parse tree produced by D96Parser#programclass.
    def visitProgramclass(self, ctx:D96Parser.ProgramclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecls.
    def visitClassdecls(self, ctx:D96Parser.ClassdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecl.
    def visitClassdecl(self, ctx:D96Parser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#superclasslist.
    def visitSuperclasslist(self, ctx:D96Parser.SuperclasslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parentlist.
    def visitParentlist(self, ctx:D96Parser.ParentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parentlst.
    def visitParentlst(self, ctx:D96Parser.ParentlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parent1.
    def visitParent1(self, ctx:D96Parser.Parent1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#otherparents.
    def visitOtherparents(self, ctx:D96Parser.OtherparentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#otherparent.
    def visitOtherparent(self, ctx:D96Parser.OtherparentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#programkey.
    def visitProgramkey(self, ctx:D96Parser.ProgramkeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classkey.
    def visitClasskey(self, ctx:D96Parser.ClasskeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier.
    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#tail_identifier.
    def visitTail_identifier(self, ctx:D96Parser.Tail_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#tailiden.
    def visitTailiden(self, ctx:D96Parser.TailidenContext):
        return self.visitChildren(ctx)



del D96Parser