grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// program: mptype 'main' LB RB LP body? RP EOF;
// mptype: INTTYPE | VOIDTYPE;
// body: funcall SEMI;
// exp: funcall | INTLIT;
// funcall: ID LB exp? RB;
// INTTYPE: 'int';
// VOIDTYPE: 'void';
// ID: [a-zA-Z]+;
// INTLIT: [0-9]+;
// LB: '(';
// RB: ')';
// LP: '{';
// RP: '}';
// SEMI: ';';



program: classdecls programclass EOF;
//syntax
	// programclass declare
programclass: classkey programkey 'main' LP RP LB 'programclassbody' RB;
	// list of class declare
classdecls: classdecl classdecls | classdecl;
	// class declare
classdecl: classkey identifier superclasslist LB 'classbody' RB;
	// parent class list;
superclasslist:parentlist| ;
parentlist: COLON parentlst;
parentlst: parent1 otherparents;
parent1: identifier;
otherparents: otherparent | ;
otherparent: CM parent1 otherparent | CM parent1;



// essential syntax===========================================
programkey:'Program';
classkey:'Class';
identifier: CHAR_SEQ tail_identifier;
tail_identifier: tailiden| ;
tailiden: (CHAR|NUM|UNDERCORE) tailiden | (CHAR|NUM|UNDERCORE);




//token===================================================
CHAR_SEQ:[A-Za-z]+;
CHAR: [A-Za-z];
NUM:[0-9];
NUM_SEQ:[0-9]+;
UNDERCORE:'_';
LB:'{';
RB:'}';
LP:'(';
RP:')';
SM:';';
CM:',';
COLON:':';


WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;