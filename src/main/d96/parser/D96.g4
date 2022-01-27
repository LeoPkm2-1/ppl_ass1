grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// program: mptype 'main' LB RB LP body? RP EOF; mptype: INTTYPE | VOIDTYPE; body: funcall SEMI;
// exp: funcall | INTLIT; funcall: ID LB exp? RB; INTTYPE: 'int'; VOIDTYPE: 'void'; ID: [a-zA-Z]+;
// INTLIT: [0-9]+; LB: '('; RB: ')'; LP: '{'; RP: '}'; SEMI: ';';

// program = classdecls (nhieu khai bao class) + programclass (class program)
program: classdecls EOF;

classdecls
	: classdecl classdecls
	| classdecl;

// classdecl
// 	: CLASS CLASSNAME (COLON CLASSNAME)? LB classbody  RB;

classdecl: CLASS IDENTIFIER parentclassname LB classbody RB;

parentclassname: (COLON IDENTIFIER)| ;


classbody: classelements| ;

classelements: classelement classelements| classelement;

// class element = vardecl or functiondecl
classelement: COMMENT |attributedecl;//|methoddecl;


attributedecl: attribute_key_decl var_list COLON var_typ_and_inital SM;



attribute_key_decl
	: VAR
	| VAL;

var_list: var_name CM var_list| var_name;

var_name: IDENTIFIER|STATIC_IDENTIFIER;

var_typ_and_inital: primitive_typ_and_inital| array_typ_and_inital;// array_typ_and_inital;

array_typ_and_inital:arr_index_inital|arr_multi_dimension_inital;

arr_multi_dimension_inital:ARRAY LP(arr_multi_dimension_inital|) RP;
multi_dimension_arr_typ: ARRAY LSB (multi_dimension_arr_typ|index_arr_typ) CM integer_literal RSB;

arr_index_inital
	:arr_index_int_list_inital
	|arr_index_bool_list_inital
	|arr_index_float_list_inital
	|arr_index_string_list_inital;

index_arr_typ
	:index_arr_int_typ
	|index_arr_bool_typ
	|index_arr_float_typ
	|index_arr_string_typ;

index_arr_int_typ: ARRAY LSB INT_TYP CM integer_literal RSB;
index_arr_bool_typ: ARRAY LSB BOOLEAN_TYP CM integer_literal RSB;
index_arr_float_typ: ARRAY LSB FLOAT_TYP CM integer_literal RSB;
index_arr_string_typ:ARRAY LSB STRING_TYP CM integer_literal RSB;

arr_index_int_list_inital: index_arr_int_typ arr_index_int_initals;

arr_index_int_initals: EQUALSIGN arr_index_int_initals_values| ;
arr_index_int_initals_values:index_array_int_literal CM arr_index_int_initals_values| index_array_int_literal;


// ======================================================================

arr_index_bool_list_inital: index_arr_bool_typ arr_index_bool_initals;

arr_index_bool_initals: EQUALSIGN arr_index_bool_initals_values| ;
arr_index_bool_initals_values:index_array_bool_literal CM arr_index_bool_initals_values| index_array_bool_literal;


// ======================================================================

arr_index_float_list_inital: index_arr_float_typ arr_index_float_initals;

arr_index_float_initals: EQUALSIGN arr_index_float_initals_values| ;
arr_index_float_initals_values:index_array_float_literal CM arr_index_float_initals_values| index_array_float_literal;


// ======================================================================

arr_index_string_list_inital: index_arr_string_typ arr_index_string_initals;

arr_index_string_initals: EQUALSIGN arr_index_string_initals_values| ;
arr_index_string_initals_values:index_array_string_literal CM arr_index_string_initals_values| index_array_string_literal;


// ======================================================================




primitive_typ_and_inital
	: attribute_int_list_intial
	| attribute_bool_list_intial
	| attribute_float_list_intial
	| attribute_string_list_intial ;

		// int intial list_intial
		attribute_int_list_intial: INT_TYP int_values_inital;

		int_values_inital: EQUALSIGN int_values_init| ;

		int_values_init: int_value_init CM int_values_init | int_value_init;

		int_value_init: IDENTIFIER|STATIC_IDENTIFIER|integer_literal; // insert int expresion


		// bool intial list_intial
		attribute_bool_list_intial: BOOLEAN_TYP bool_values_inital; 

		bool_values_inital: EQUALSIGN bool_values_init| ;

		bool_values_init: bool_value_init CM bool_values_init | bool_value_init;

		bool_value_init	: IDENTIFIER| STATIC_IDENTIFIER	| BOOLEAN_LITERAL; // insert bool expresion

		// float intial list_intial
		attribute_float_list_intial: FLOAT_TYP float_values_inital;

		float_values_inital: EQUALSIGN float_values_init| ;

		float_values_init: float_value_init CM float_values_init | float_value_init;

		float_value_init: IDENTIFIER|STATIC_IDENTIFIER|FLOAT_LITERAL; // insert float expresion


		// string intial list_intial
		attribute_string_list_intial: STRING_TYP string_values_inital;

		string_values_inital: EQUALSIGN string_values_init| ;

		string_values_init: string_value_init CM string_values_init | string_value_init;

		string_value_init: IDENTIFIER|STATIC_IDENTIFIER|STRING_LITERAL; // insert string expresion


// integer literal
integer_literal
	: INTEGER_LITERAL_X10
	| INTEGER_LITERAL_X16
	| INTEGER_LITERAL_X8
	| INTEGER_LITERAL_X2
	;


// token Literals
//integer Literals
// INTEGER_LITERAL: INTEGER_LITERAL_X10 {self.text=self.text.replace("_","")}
// 	|INTEGER_LITERAL_X16 {self.text=self.text.replace("_","")}
// 	|INTEGER_LITERAL_X8 {self.text=self.text.replace("_","")}
// 	|INTEGER_LITERAL_X2 {self.text=self.text.replace("_","")};
	//base 10
INTEGER_LITERAL_X10
	: [1-9] NUMBERDIGIT* ('_'NUMBERDIGIT+)* {self.text=self.text.replace("_","")}
	|'0' ;

	//base 16
INTEGER_LITERAL_X16
	:('0x'|'0X')[1-9A-F] X16DIGIT* ('_' X16DIGIT+)* { self.text=self.text.replace("_","") }
	|('0x0'|'0X0');
	
	//base 8
INTEGER_LITERAL_X8
	:'0'[1-7] X8DIGIT* ('_'X8DIGIT+)* { self.text=self.text.replace("_","") }
	|('00');
	
	//base 2
INTEGER_LITERAL_X2
	:('0b'|'0B')'1' X2DIGIT* ('_'X2DIGIT+)* { self.text=self.text.replace("_","") }
	|('0b0'|'0B0');

fragment NUMBERDIGIT:[0-9];
fragment X16DIGIT:[0-9A-F];
fragment X8DIGIT:[0-7];
fragment X2DIGIT:[0-1];

//float Literals
FLOAT_LITERAL
	: FLOAT_INT_COMPO FLOAT_DECIMAL_COMPO { self.text=self.text.replace("_","") }
	| FLOAT_INT_COMPO FLOAT_EXPO_COMPO { self.text=self.text.replace("_","") }
	| FLOAT_DECIMAL_COMPO FLOAT_EXPO_COMPO
	| FLOAT_INT_COMPO FLOAT_DECIMAL_COMPO FLOAT_EXPO_COMPO { self.text=self.text.replace("_","") };
	
fragment FLOAT_INT_COMPO: [1-9] NUMBERDIGIT* ('_'NUMBERDIGIT+)* |'0' ;
fragment FLOAT_DECIMAL_COMPO: '.'NUMBERDIGIT*;
fragment FLOAT_EXPO_COMPO: [eE] [-+]? NUMBERDIGIT+;

COMMENT: ('##' (.)*? '##') -> skip;

//boolean Literals
BOOLEAN_LITERAL
	: 'True'
	| 'False'
	;

// string Literals
STRING_LITERAL
	: '"' CHARACTER* '"'
	{
		inputstr=str(self.text)
		self.text=inputstr[1:-1]
	}
	;

fragment CHARACTER
	: ~[\b\f\r\n\t"'\\]|ESCAPE_CHAR|DOUBLE_QUOTE_IN_STRING
	;

fragment ESCAPE_CHAR
	: '\\' [bfrnt'\\]
	;

fragment DOUBLE_QUOTE_IN_STRING
	:'\'"'
	;

fragment ESCAPE_CHAR_ILEGAL
	: '\\' ~[bfrnt'\\] 
	| ~'\\'
	;

		

	//==========================================================================================================================================
															// STRING_LITERAL
															// 	:'"' CHARACTER* '"'
															// 	{
															// 		inputstr=str(self.text)
															// 		self.text=inputstr[1:-1]
															// 	}
															// 	;

															// fragment CHARACTER
															// :  ~[\b\t\n\f\r"'\\]
															// |ESCAPE_CHAR
															// ;
															// // fragment ESCAPE_CHAR: ('\\b'|'\\f'|'\\r'|'\\n'|'\\t'|'\\\''|'\\\\');
															
															// fragment ESCAPE_CHAR: '\\' [btnfr'\\]|'\'"' ;
															// // fragment ESCAPE_CHAR_ILEGAL: '\\'~[bfrnt"'\\]  ~'\\' ;
															// fragment ESCAPE_CHAR_ILEGAL: '\\' ~[btnfr'\\] | ~'\\' ;
															// 	// 		fragment
															// 	// ESC : '\\"' | '\\\\' ; // 2-char sequences \" and \\

	//==========================================================================================================================================

// array Literals
// index_array_literal:;
index_array_literal:index_array_int_literal| index_array_bool_literal| index_array_string_literal| index_array_float_literal;

index_array_int_literal: ARRAY LP int_values_init RP;	
index_array_bool_literal: ARRAY LP bool_values_init RP;	
index_array_string_literal: ARRAY LP string_values_init RP;	
index_array_float_literal: ARRAY LP float_values_init RP;

// multi_dimension_array_literal
multi_dimension_array_literal: ARRAY LP elements_multi_dimension_arr RP;
elements_multi_dimension_arr: elem_multi_dimension_arr CM elements_multi_dimension_arr| elem_multi_dimension_arr;
elem_multi_dimension_arr: multi_dimension_array_literal| index_array_literal;

CLASS:'Class';
ARRAY:'Array';
VAR:'Var';
VAL:'Val';
LP:'(';
RP:')';
LB:'{';
RB:'}';
LSB:'[';
RSB:']';
SM:';';
CM:',';
COLON:':';
EQUALSIGN:'=';
BOOLEAN_TYP:'Boolean';
INT_TYP:'Int';
FLOAT_TYP:'Float';
STRING_TYP:'String';
IDENTIFIER:([A-Za-z]|'_')+ ([A-Za-z0-9]|'_')* ;
fragment DOLAR_SIGN:'$';
STATIC_IDENTIFIER: DOLAR_SIGN [A-Za-z_]+ [A-Za-z_0-9]* ;



WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


// UNCLOSE_STRING
// 	: '"' CHARACTER* END_A_LINE_SIGN
// 	{
// 		unclose_string = str(self.text)
// 		end_sign=['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
// 		i=len(a)
// 		if unclose_string[i-1] in end_sign:
// 			raise UncloseString(unclose_string[1:-1])
// 		else:
// 			raise UncloseString(unclose_string[1:])
// 	}
// 	;
UNCLOSE_STRING
	: '"' CHARACTER* END_A_LINE_SIGN 
	{ 
		unclose_str=str(self.text)
		raise UncloseString(unclose_str[1:])
	};

fragment END_A_LINE_SIGN
	: [\b\t\n\f\r"'\\] | EOF
	;

ILLEGAL_ESCAPE
	: '"' CHARACTER* ESCAPE_CHAR_ILEGAL
	{
		ilegal = str(self.text)
		raise IllegalEscape(ilegal[1:])
	}
	;

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;