# Generated from d:\extened-PPL\initial\initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\5\2\25\n\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5%\n\5\f\5\16\5(")
        buf.write("\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\61\n\6\3\7\3\7\3")
        buf.write("\7\5\7\66\n\7\3\7\3\7\3\7\2\3\b\b\2\4\6\b\n\f\2\3\3\2")
        buf.write("\4\5\29\2\16\3\2\2\2\4\31\3\2\2\2\6\33\3\2\2\2\b\36\3")
        buf.write("\2\2\2\n\60\3\2\2\2\f\62\3\2\2\2\16\17\5\4\3\2\17\20\7")
        buf.write("\3\2\2\20\21\7\n\2\2\21\22\7\13\2\2\22\24\7\f\2\2\23\25")
        buf.write("\5\6\4\2\24\23\3\2\2\2\24\25\3\2\2\2\25\26\3\2\2\2\26")
        buf.write("\27\7\r\2\2\27\30\7\2\2\3\30\3\3\2\2\2\31\32\t\2\2\2\32")
        buf.write("\5\3\2\2\2\33\34\5\f\7\2\34\35\7\16\2\2\35\7\3\2\2\2\36")
        buf.write("\37\b\5\1\2\37 \5\n\6\2 &\3\2\2\2!\"\f\4\2\2\"#\7\t\2")
        buf.write("\2#%\5\n\6\2$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2")
        buf.write("\'\t\3\2\2\2(&\3\2\2\2)*\7\n\2\2*+\5\b\5\2+,\7\13\2\2")
        buf.write(",\61\3\2\2\2-\61\5\f\7\2.\61\7\7\2\2/\61\7\b\2\2\60)\3")
        buf.write("\2\2\2\60-\3\2\2\2\60.\3\2\2\2\60/\3\2\2\2\61\13\3\2\2")
        buf.write("\2\62\63\7\6\2\2\63\65\7\n\2\2\64\66\5\b\5\2\65\64\3\2")
        buf.write("\2\2\65\66\3\2\2\2\66\67\3\2\2\2\678\7\13\2\28\r\3\2\2")
        buf.write("\2\6\24&\60\65")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'int'", "'void'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'('", "')'", "'{'", 
                     "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTTYPE", "VOIDTYPE", "ID", 
                      "INTLIT", "FLOATLIT", "ADD", "LB", "RB", "LP", "RP", 
                      "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_exp1 = 4
    RULE_funcall = 5

    ruleNames =  [ "program", "mptype", "body", "exp", "exp1", "funcall" ]

    EOF = Token.EOF
    T__0=1
    INTTYPE=2
    VOIDTYPE=3
    ID=4
    INTLIT=5
    FLOATLIT=6
    ADD=7
    LB=8
    RB=9
    LP=10
    RP=11
    SEMI=12
    WS=13
    ERROR_CHAR=14
    UNCLOSE_STRING=15
    ILLEGAL_ESCAPE=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MT22Parser.MptypeContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(MT22Parser.BodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.mptype()
            self.state = 13
            self.match(MT22Parser.T__0)
            self.state = 14
            self.match(MT22Parser.LB)
            self.state = 15
            self.match(MT22Parser.RB)
            self.state = 16
            self.match(MT22Parser.LP)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.ID:
                self.state = 17
                self.body()


            self.state = 20
            self.match(MT22Parser.RP)
            self.state = 21
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MT22Parser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MT22Parser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_mptype




    def mptype(self):

        localctx = MT22Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            _la = self._input.LA(1)
            if not(_la==MT22Parser.INTTYPE or _la==MT22Parser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MT22Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_body




    def body(self):

        localctx = MT22Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.funcall()
            self.state = 26
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(MT22Parser.Exp1Context,0)


        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.exp1()
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 31
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 32
                    self.match(MT22Parser.ADD)
                    self.state = 33
                    self.exp1() 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def funcall(self):
            return self.getTypedRuleContext(MT22Parser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp1




    def exp1(self):

        localctx = MT22Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exp1)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(MT22Parser.LB)
                self.state = 40
                self.exp(0)
                self.state = 41
                self.match(MT22Parser.RB)
                pass
            elif token in [MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.funcall()
                pass
            elif token in [MT22Parser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(MT22Parser.INTLIT)
                pass
            elif token in [MT22Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(MT22Parser.FLOATLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcall




    def funcall(self):

        localctx = MT22Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MT22Parser.ID)
            self.state = 49
            self.match(MT22Parser.LB)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.ID) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.LB))) != 0):
                self.state = 50
                self.exp(0)


            self.state = 53
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




