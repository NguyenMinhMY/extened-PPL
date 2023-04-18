'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from Visitor import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
# from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntegerType()), CName(self.libName)),
                    Symbol("putInt", MType([IntegerType()], VoidType()), CName(self.libName))      
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class StringType(Type):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, sym):
        #frame: Frame
        #sym: List[Symbol]
        # self.frame = frame

        self.sym = sym

class Access():
    def __init__(self, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean
        # self.frame = frame

        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".asm")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        e = SubBody(self.env)
        for x in ast.decls:
            e = self.visit(x, e)
        # generate default constructor
        # self.genMETHOD(FuncDecl("<init>", None, list(), None, BlockStmt( list())), c)
        
        self.emit.mapping()
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o):
        #consdecl: FuncDecl
        #o: Any
        
        glenv = o
        body = consdecl.body
        list(map(lambda x: self.visit(x, SubBody(glenv)), body.body))

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        self.genMETHOD(ast, subctxt.sym)
        return SubBody([Symbol(ast.name, MType(list(), ast.return_type), CName(self.className))] + subctxt.sym)

    def visitFuncCall(self, ast, o):
        #ast: FuncCall
        #o: Any
        # Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)
        # ctxt = o
        # frame = ctxt.frame
        # nenv = ctxt.sym
        # sym = self.lookup(ast.name, nenv, lambda x: x.name)
        # cname = sym.value.value
    
        # ctype = sym.mtype

        # in_ = ("", list())
        # for x in ast.args:
        #     str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
        #     in_ = (in_[0] + str1, in_[1].append(typ1))
        # self.emit.printout(in_[0])
        # self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, frame))
        ctxt = o
        # frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name, nenv, lambda x: x.name)
        # cname = sym.value.value
        # ctype = sym.mtype
        in_ = ("", list())

        resReg = None
        for x in ast.args:
            str1, typ1 = self.visit(x, Access(nenv, False, True))
            in_ = (in_[0] + str1[0], in_[1].append(typ1))
            resReg = str1[1]
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitMOVE("$a0", resReg))
        self.emit.printout(self.emit.emitICALLPRINT())
        self.emit.printout(self.emit.emitSYSCALL())

    def visitIntegerLit(self, ast, o):
        #ast: IntLiteral
        #o: Any

        # ctxt = o
        # frame = ctxt.frame
        # return self.emit.emitPUSHICONST(ast.val, frame), IntegerType()
        return self.emit.emitILOAD(ast.val), IntegerType()
    
    def visitFloatLit(self, ast, o):
        #ast: FloatLiteral
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.val), frame), FloatType()
    
    def visitBinExpr(self, ast, o):

        lexem = ast.op
        left = ast.left
        right = ast.right

        (instrLeft, regLeft), typLeft = self.visit(left,o)
        self.emit.printout(instrLeft)

        (instrRight, regRight), typRight = self.visit(right,o)
        self.emit.printout(instrRight)

        return self.emit.emitADD(regLeft,regRight), IntegerType()
            
        # # ast: BinExpr
        # # o: any
        # ctxt = o
        
        # lexem = ast.op
        # left = ast.left
        # right = ast.right
        # str_left, typ_left = self.visit(left,ctxt)

        # str_right, typ_right = self.visit(right,ctxt)
        # if type(typ_left) is FloatType or type(typ_right) is FloatType:
        #     self.emit.printout(str_left)
        #     if type(typ_left) is IntegerType:
        #         str_i2f = self.emit.emitI2F(ctxt.frame)
        #         self.emit.printout(str_i2f)

        #     self.emit.printout(str_right)
        #     if type(typ_right) is IntegerType:
        #         str_i2f = self.emit.emitI2F(ctxt.frame)
        #         self.emit.printout(str_i2f)
        #     return self.emit.emitADDOP(lexem, FloatType(), ctxt.frame), FloatType()    
        # else:
        #     self.emit.printout(str_left)
        #     self.emit.printout(str_right)
        #     return self.emit.emitADDOP(lexem, IntegerType(),ctxt.frame), IntegerType()





        
    
