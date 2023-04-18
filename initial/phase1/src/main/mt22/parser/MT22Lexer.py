# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\6\5\67\n\5\r\5\16\58\3\6\6\6<\n\6\r\6\16\6=\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7P\n\7\3\b\3\b\7\bT\n\b\f\b\16\bW\13\b\3\t\3")
        buf.write("\t\5\t[\n\t\3\t\6\t^\n\t\r\t\16\t_\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\6\20o\n\20\r\20")
        buf.write("\16\20p\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\2\2\24")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\2\23\t\25\n\27\13\31")
        buf.write("\f\33\r\35\16\37\17!\20#\21%\22\3\2\7\4\2C\\c|\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2\u0080\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5,\3\2\2\2\7\60")
        buf.write("\3\2\2\2\t\66\3\2\2\2\13;\3\2\2\2\rO\3\2\2\2\17Q\3\2\2")
        buf.write("\2\21X\3\2\2\2\23a\3\2\2\2\25c\3\2\2\2\27e\3\2\2\2\31")
        buf.write("g\3\2\2\2\33i\3\2\2\2\35k\3\2\2\2\37n\3\2\2\2!t\3\2\2")
        buf.write("\2#v\3\2\2\2%x\3\2\2\2\'(\7o\2\2()\7c\2\2)*\7k\2\2*+\7")
        buf.write("p\2\2+\4\3\2\2\2,-\7k\2\2-.\7p\2\2./\7v\2\2/\6\3\2\2\2")
        buf.write("\60\61\7x\2\2\61\62\7q\2\2\62\63\7k\2\2\63\64\7f\2\2\64")
        buf.write("\b\3\2\2\2\65\67\t\2\2\2\66\65\3\2\2\2\678\3\2\2\28\66")
        buf.write("\3\2\2\289\3\2\2\29\n\3\2\2\2:<\t\3\2\2;:\3\2\2\2<=\3")
        buf.write("\2\2\2=;\3\2\2\2=>\3\2\2\2>\f\3\2\2\2?@\5\13\6\2@A\5\17")
        buf.write("\b\2AB\5\21\t\2BC\b\7\2\2CP\3\2\2\2DE\5\13\6\2EF\5\17")
        buf.write("\b\2FG\b\7\3\2GP\3\2\2\2HI\5\13\6\2IJ\5\21\t\2JK\b\7\4")
        buf.write("\2KP\3\2\2\2LM\5\17\b\2MN\5\21\t\2NP\3\2\2\2O?\3\2\2\2")
        buf.write("OD\3\2\2\2OH\3\2\2\2OL\3\2\2\2P\16\3\2\2\2QU\7\60\2\2")
        buf.write("RT\t\3\2\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\20")
        buf.write("\3\2\2\2WU\3\2\2\2XZ\t\4\2\2Y[\t\5\2\2ZY\3\2\2\2Z[\3\2")
        buf.write("\2\2[]\3\2\2\2\\^\t\3\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2")
        buf.write("\2_`\3\2\2\2`\22\3\2\2\2ab\7-\2\2b\24\3\2\2\2cd\7*\2\2")
        buf.write("d\26\3\2\2\2ef\7+\2\2f\30\3\2\2\2gh\7}\2\2h\32\3\2\2\2")
        buf.write("ij\7\177\2\2j\34\3\2\2\2kl\7=\2\2l\36\3\2\2\2mo\t\6\2")
        buf.write("\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2qr\3\2\2\2r")
        buf.write("s\b\20\5\2s \3\2\2\2tu\13\2\2\2u\"\3\2\2\2vw\13\2\2\2")
        buf.write("w$\3\2\2\2xy\13\2\2\2y&\3\2\2\2\n\28=OUZ_p\6\3\7\2\3\7")
        buf.write("\3\3\7\4\b\2\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    FLOATLIT = 6
    ADD = 7
    LB = 8
    RB = 9
    LP = 10
    RP = 11
    SEMI = 12
    WS = 13
    ERROR_CHAR = 14
    UNCLOSE_STRING = 15
    ILLEGAL_ESCAPE = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'+'", "'('", "')'", "'{'", "'}'", 
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "FLOATLIT", "ADD", "LB", 
            "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "FLOATLIT", 
                  "DECPART", "EXPPART", "ADD", "LB", "RB", "LP", "RP", "SEMI", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.FLOATLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            self.text = self.text.replace("_", "");

     

        if actionIndex == 1:

            self.text = self.text.replace("_", "");

     

        if actionIndex == 2:

            self.text = self.text.replace("_", "");

     


