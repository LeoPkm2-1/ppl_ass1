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


    # Visit a parse tree produced by D96Parser#var_name.
    def visitVar_name(self, ctx:D96Parser.Var_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_typ_and_inital.
    def visitVar_typ_and_inital(self, ctx:D96Parser.Var_typ_and_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_typ_and_inital.
    def visitArray_typ_and_inital(self, ctx:D96Parser.Array_typ_and_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_multi_dimension_inital.
    def visitArr_multi_dimension_inital(self, ctx:D96Parser.Arr_multi_dimension_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_dimension_arr_typ.
    def visitMulti_dimension_arr_typ(self, ctx:D96Parser.Multi_dimension_arr_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_inital.
    def visitArr_index_inital(self, ctx:D96Parser.Arr_index_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_arr_typ.
    def visitIndex_arr_typ(self, ctx:D96Parser.Index_arr_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_arr_int_typ.
    def visitIndex_arr_int_typ(self, ctx:D96Parser.Index_arr_int_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_arr_bool_typ.
    def visitIndex_arr_bool_typ(self, ctx:D96Parser.Index_arr_bool_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_arr_float_typ.
    def visitIndex_arr_float_typ(self, ctx:D96Parser.Index_arr_float_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_arr_string_typ.
    def visitIndex_arr_string_typ(self, ctx:D96Parser.Index_arr_string_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_int_list_inital.
    def visitArr_index_int_list_inital(self, ctx:D96Parser.Arr_index_int_list_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_int_initals.
    def visitArr_index_int_initals(self, ctx:D96Parser.Arr_index_int_initalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_int_initals_values.
    def visitArr_index_int_initals_values(self, ctx:D96Parser.Arr_index_int_initals_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_bool_list_inital.
    def visitArr_index_bool_list_inital(self, ctx:D96Parser.Arr_index_bool_list_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_bool_initals.
    def visitArr_index_bool_initals(self, ctx:D96Parser.Arr_index_bool_initalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_bool_initals_values.
    def visitArr_index_bool_initals_values(self, ctx:D96Parser.Arr_index_bool_initals_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_float_list_inital.
    def visitArr_index_float_list_inital(self, ctx:D96Parser.Arr_index_float_list_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_float_initals.
    def visitArr_index_float_initals(self, ctx:D96Parser.Arr_index_float_initalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_float_initals_values.
    def visitArr_index_float_initals_values(self, ctx:D96Parser.Arr_index_float_initals_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_string_list_inital.
    def visitArr_index_string_list_inital(self, ctx:D96Parser.Arr_index_string_list_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_string_initals.
    def visitArr_index_string_initals(self, ctx:D96Parser.Arr_index_string_initalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_index_string_initals_values.
    def visitArr_index_string_initals_values(self, ctx:D96Parser.Arr_index_string_initals_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_typ_and_inital.
    def visitPrimitive_typ_and_inital(self, ctx:D96Parser.Primitive_typ_and_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_int_list_intial.
    def visitAttribute_int_list_intial(self, ctx:D96Parser.Attribute_int_list_intialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_values_inital.
    def visitInt_values_inital(self, ctx:D96Parser.Int_values_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_values_init.
    def visitInt_values_init(self, ctx:D96Parser.Int_values_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_value_init.
    def visitInt_value_init(self, ctx:D96Parser.Int_value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_bool_list_intial.
    def visitAttribute_bool_list_intial(self, ctx:D96Parser.Attribute_bool_list_intialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bool_values_inital.
    def visitBool_values_inital(self, ctx:D96Parser.Bool_values_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bool_values_init.
    def visitBool_values_init(self, ctx:D96Parser.Bool_values_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bool_value_init.
    def visitBool_value_init(self, ctx:D96Parser.Bool_value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_float_list_intial.
    def visitAttribute_float_list_intial(self, ctx:D96Parser.Attribute_float_list_intialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_values_inital.
    def visitFloat_values_inital(self, ctx:D96Parser.Float_values_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_values_init.
    def visitFloat_values_init(self, ctx:D96Parser.Float_values_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_value_init.
    def visitFloat_value_init(self, ctx:D96Parser.Float_value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_string_list_intial.
    def visitAttribute_string_list_intial(self, ctx:D96Parser.Attribute_string_list_intialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_values_inital.
    def visitString_values_inital(self, ctx:D96Parser.String_values_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_values_init.
    def visitString_values_init(self, ctx:D96Parser.String_values_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_value_init.
    def visitString_value_init(self, ctx:D96Parser.String_value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#integer_literal.
    def visitInteger_literal(self, ctx:D96Parser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_array_literal.
    def visitIndex_array_literal(self, ctx:D96Parser.Index_array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_array_int_literal.
    def visitIndex_array_int_literal(self, ctx:D96Parser.Index_array_int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_array_bool_literal.
    def visitIndex_array_bool_literal(self, ctx:D96Parser.Index_array_bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_array_string_literal.
    def visitIndex_array_string_literal(self, ctx:D96Parser.Index_array_string_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_array_float_literal.
    def visitIndex_array_float_literal(self, ctx:D96Parser.Index_array_float_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_dimension_array_literal.
    def visitMulti_dimension_array_literal(self, ctx:D96Parser.Multi_dimension_array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elements_multi_dimension_arr.
    def visitElements_multi_dimension_arr(self, ctx:D96Parser.Elements_multi_dimension_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elem_multi_dimension_arr.
    def visitElem_multi_dimension_arr(self, ctx:D96Parser.Elem_multi_dimension_arrContext):
        return self.visitChildren(ctx)



del D96Parser