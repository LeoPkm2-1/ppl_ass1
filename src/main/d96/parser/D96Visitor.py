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


    # Visit a parse tree produced by D96Parser#methoddecl.
    def visitMethoddecl(self, ctx:D96Parser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#norm_methoddecl.
    def visitNorm_methoddecl(self, ctx:D96Parser.Norm_methoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor_methoddecl.
    def visitConstructor_methoddecl(self, ctx:D96Parser.Constructor_methoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor_methoddecl.
    def visitDestructor_methoddecl(self, ctx:D96Parser.Destructor_methoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#con_des_functionbody.
    def visitCon_des_functionbody(self, ctx:D96Parser.Con_des_functionbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmts.
    def visitStmts(self, ctx:D96Parser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlsts.
    def visitParamlsts(self, ctx:D96Parser.ParamlstsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paralst.
    def visitParalst(self, ctx:D96Parser.ParalstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramtyp.
    def visitParamtyp(self, ctx:D96Parser.ParamtypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primityp.
    def visitPrimityp(self, ctx:D96Parser.PrimitypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrtyp.
    def visitArrtyp(self, ctx:D96Parser.ArrtypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#functionbody.
    def visitFunctionbody(self, ctx:D96Parser.FunctionbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributedecl.
    def visitAttributedecl(self, ctx:D96Parser.AttributedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcvardecl.
    def visitFuncvardecl(self, ctx:D96Parser.FuncvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_key_dec.
    def visitVar_key_dec(self, ctx:D96Parser.Var_key_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_list.
    def visitAttribute_list(self, ctx:D96Parser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_list.
    def visitVar_list(self, ctx:D96Parser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attibute_name.
    def visitAttibute_name(self, ctx:D96Parser.Attibute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_typ_and_inital.
    def visitVar_typ_and_inital(self, ctx:D96Parser.Var_typ_and_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_op_arr.
    def visitIndex_op_arr(self, ctx:D96Parser.Index_op_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr11.
    def visitExpr11(self, ctx:D96Parser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr12.
    def visitExpr12(self, ctx:D96Parser.Expr12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call_function.
    def visitCall_function(self, ctx:D96Parser.Call_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#str_op.
    def visitStr_op(self, ctx:D96Parser.Str_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#comp_op.
    def visitComp_op(self, ctx:D96Parser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logic_op.
    def visitLogic_op(self, ctx:D96Parser.Logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#add_sub_op.
    def visitAdd_sub_op(self, ctx:D96Parser.Add_sub_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mul_divs_op.
    def visitMul_divs_op(self, ctx:D96Parser.Mul_divs_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_typ_and_inital.
    def visitArray_typ_and_inital(self, ctx:D96Parser.Array_typ_and_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_multi_dimension_inital.
    def visitArr_multi_dimension_inital(self, ctx:D96Parser.Arr_multi_dimension_initalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_multi_dimension_initals.
    def visitArr_multi_dimension_initals(self, ctx:D96Parser.Arr_multi_dimension_initalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_multi_dimension_initals_values.
    def visitArr_multi_dimension_initals_values(self, ctx:D96Parser.Arr_multi_dimension_initals_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_dimension_arr_typ.
    def visitMulti_dimension_arr_typ(self, ctx:D96Parser.Multi_dimension_arr_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_dimension_arr_elem_typ.
    def visitMulti_dimension_arr_elem_typ(self, ctx:D96Parser.Multi_dimension_arr_elem_typContext):
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