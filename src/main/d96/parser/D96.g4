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

classdecls:INTEGER_LITERAL_X10;

// token Literals
	//integer
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
	//float
		FLOAT_LITERAL
			: FLOAT_INT_COMPO FLOAT_DECIMAL_COMPO
			| FLOAT_INT_COMPO FLOAT_EXPO_COMPO
			|
			
			FLOAT_INT_COMPO FLOAT_DECIMAL_COMPO FLOAT_EXPO_COMPO;
		fragment FLOAT_INT_COMPO: [1-9] NUMBERDIGIT* ('_'NUMBERDIGIT+)* |'0' ;
		fragment FLOAT_DECIMAL_COMPO: '.'NUMBERDIGIT*;
		fragment FLOAT_EXPO_COMPO: [eE] [-+]? NUMBERDIGIT+;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;