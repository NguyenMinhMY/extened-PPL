from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([FuncDecl("main",
			self.visit(ctx.mptype()),
                        [],
                        None,
                        BlockStmt([self.visit(ctx.body())] if ctx.body() else []))])

    def visitMptype(self,ctx:MT22Parser.MptypeContext):
        if ctx.INTTYPE():
            return IntegerType()
        else:
            return VoidType()

    def visitBody(self,ctx:MT22Parser.BodyContext):
        return self.visit(ctx.funcall())
  
  	
    def visitFuncall(self,ctx:MT22Parser.FuncallContext):
        return FuncCall(ctx.ID().getText(),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:MT22Parser.ExpContext):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        else:
            return IntegerLit(int(ctx.INTLIT().getText()))
