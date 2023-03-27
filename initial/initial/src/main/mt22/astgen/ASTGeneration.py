from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program  : mptype 'main' LB RB LP body? RP EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([FuncDecl("main",
			self.visit(ctx.mptype()),
                        [],
                        None,
                        BlockStmt([self.visit(ctx.body())] if ctx.body() else []))])


    # mptype: INTTYPE | VOIDTYPE ;
    def visitMptype(self, ctx:MT22Parser.MptypeContext):
        if ctx.INTTYPE():
            return IntegerType()
        else:
            return VoidType()


    # body: funcall SEMI;
    def visitBody(self, ctx:MT22Parser.BodyContext):
        return self.visit(ctx.funcall())


    # exp: exp ADD exp1 | exp1;
    def visitExp(self, ctx:MT22Parser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1())
        else:
            return BinExpr(ctx.ADD().getText(), self.visit(ctx.exp()), self.visit(ctx.exp1()))


    # exp1: LB exp RB | funcall | INTLIT | FLOATLIT;
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            floatlit = ctx.FLOATLIT().getText()
            if floatlit[0] == '.':
                floatlit = '0' + floatlit
            return FloatLit(float(floatlit))
        else:
            return self.visit(ctx.funcall())



    # funcall: ID LB exp? RB ;
    def visitFuncall(self, ctx:MT22Parser.FuncallContext):
        if ctx.getChildCount() == 3:
            return FuncCall(ctx.ID().getText(), [])
        else:
            return FuncCall(ctx.ID().getText(), [self.visit(ctx.exp())])
