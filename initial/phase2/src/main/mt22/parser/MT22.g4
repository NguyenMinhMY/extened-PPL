grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: exp ADD exp1 | exp1;
exp1: LB exp RB | funcall | INTLIT | FLOATLIT;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;
FLOATLIT: INTLIT DECPART EXPPART {
self.text = self.text.replace("_", "");
} | INTLIT DECPART {
self.text = self.text.replace("_", "");
}| INTLIT EXPPART  {
self.text = self.text.replace("_", "");
}| DECPART EXPPART;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE] [-+]? [0-9]+ ;

ADD: '+';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;