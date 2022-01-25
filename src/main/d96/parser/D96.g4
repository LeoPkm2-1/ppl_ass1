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
program: classdecls  EOF;

classdecls
	: classdecl classdecls
	| classdecl;

// classdecl
// 	: CLASS CLASSNAME (COLON CLASSNAME)? LB classbody  RB;

classdecl
	: CLASS CLASSNAME parentclassname LB classbody  RB;

parentclassname
	:(COLON CLASSNAME)| ;


classbody
	: classelements| ;

classelements
	: classelement classelements| classelement;


classelement
	:attributedecl|methoddecl;

// attributedecl
// 	:(VAL|VAR) (IDENTIFIER|STATIC_IDENTIFIER)+;

attributedecl
	:(VAL|VAR) varlist COLON typ values;

values
	:vals| ;


varlist
	: var_item CM varlist 
	|var_item;

var_item
	: IDENTIFIER
	|STATIC_IDENTIFIER;

typ
	: BOOLEAN_TYP
	| INT_TYP
	| FLOAT_TYP
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
	// index_array_literal:Array LP listarrelement LB ;


	Array:'Array';
	CLASS:'Class';
	LP:'(';
	RP:')';
	LB:'{';
	RB:'}';
	SM:';';
	CM:',';
	COLON:':';
	VAL:'Val';
	VAR:'Var';
	BOOLEAN_TYP:'Boolean';
	INT_TYP:'Int';
	FLOAT_TYP:'Float';

	IDENTIFIER:[A-Za-z_]+ [A-Za-z_0-9]* ;
	CLASSNAME:[A-Za-z_]+ [A-Za-z_0-9]* ;
	STATIC_IDENTIFIER: '$' [A-Za-z_]+ [A-Za-z_0-9]* ;



WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


UNCLOSE_STRING
	: '"' CHARACTER* END_A_LINE_SIGN
	{
		unclose_string = str(self.text)
		end_sign=['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		i=len(a)
		if unclose_string[i-1] in end_sign:
			raise UncloseString(unclose_string[1:-1])
		else:
			raise UncloseString(unclose_string[1:])
	}
	;

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