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
program: classdecls programclass EOF;
//syntax
// programclass declare => Class Program { body program }
programclass: classkey programkey LB programclassbody RB;
programclassbody: 'programclassbody';
// list of class declare: classdecl = 1 class 
classdecls: classdecl classdecls | classdecl;
// class declare => Class <id> [: <parent classes>] { class body}
classdecl: classkey identifier superclasslist LB classbody RB;
classbody: 'classbody';
// parent class list optional;
superclasslist: parentlist |;
// parent list => : <list of parents>
parentlist: COLON parentlst;
parentlst: parent1 otherparents;
parent1: identifier;
otherparents: otherparent |;
otherparent: CM parent1 otherparent | CM parent1;

// essential syntax===========================================
programkey: 'Program';
classkey: 'Class';
identifier: CHAR_SEQ tail_identifier;
tail_identifier: tailiden |;
tailiden: (CHAR | NUM | UNDERCORE) tailiden
	| (CHAR | NUM | UNDERCORE);
integer: INT_DEC | INT_OCT | INT_HEX | INT_BIN;

//token===================================================
INT_DEC:
	[1-9][0-9]* ('_' [0-9]+)* { self.text=self.text.replace("_","") }
	| '0';
INT_OCT:
	'0' [0-7]+ ('_' [0-7]+)* { self.text=self.text.replace("_","") };
INT_HEX:
	'0' [xX][0-9A-F]+ ('_' [A-F0-9]+)* { self.text=self.text.replace("_","") };
INT_BIN:
	'0' [bB][0-1]+ ('_' [0-1]+)* { self.text=self.text.replace("_","") };
FLOAT: (INT_PART DECIMAL_PART) { self.text=self.text.replace("_","") }
	| (INT_PART EXP_PART) { self.text=self.text.replace("_","") }
	| (DECIMAL_PART EXP_PART)
	| (INT_PART DECIMAL_PART EXP_PART) { self.text=self.text.replace("_","") };
fragment INT_PART: [1-9][0-9]* ('_' [0-9]+)* | '0';
fragment DECIMAL_PART: '.' [0-9]*;
fragment EXP_PART: [eE](('+' | '-')?) [0-9]+;
BOOL: 'True' | 'False';
// STRING:DBQUOTESTR (~[ DBQUOTESTR ] | SINGLEQUOTESTR DBQUOTESTR)* DBQUOTESTR;

fragment SINGLEQUOTESTR: '\'';
STRNG_LITERAL: '"' STRNG_CHARACTER* '"'{
	drawString=str(self.text)
	LengthOfDrawString=len(drawString)
	self.text=drawString[1:LengthOfDrawString-2]
};
fragment STRNG_CHARACTER: ~[\b\f\r\n\t'"\\] |ESCAPE_CHAR;
fragment ESCAPE_CHAR: '\\' [bfrnt'"\\];
fragment WRONG_ESCAPE: '\\' ~[bfrnt'"\\];


CHAR_SEQ: [A-Za-z]+;
CHAR: [A-Za-z];
NUM: [0-9];
NUM_SEQ: [0-9]+;
UNDERCORE: '_';
LB: '{';
RB: '}';
LP: '(';
RP: ')';
SM: ';';
CM: ',';
COLON: ':';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: '"' STRNG_CHARACTER* ([\b\f\r\n\t'"\\]|EOF)
	{
		y=str(self.text)	
		special_char=['\b','\f','\r','\n','t','"','\\']
		if y[-1] in special_char:
			str_len=len(y)
			raise UncloseString(y[1:str_len-1])
		else:
			raise UncloseString(y[1:])
	};
ILLEGAL_ESCAPE: .;