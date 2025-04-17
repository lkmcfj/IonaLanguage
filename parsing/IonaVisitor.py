# Generated from Iona.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IonaParser import IonaParser
else:
    from IonaParser import IonaParser

# This class defines a complete generic visitor for a parse tree produced by IonaParser.

class IonaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IonaParser#program.
    def visitProgram(self, ctx:IonaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#dataDecl.
    def visitDataDecl(self, ctx:IonaParser.DataDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#dataDeclPart.
    def visitDataDeclPart(self, ctx:IonaParser.DataDeclPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#expr1.
    def visitExpr1(self, ctx:IonaParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#expr2.
    def visitExpr2(self, ctx:IonaParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#expr3.
    def visitExpr3(self, ctx:IonaParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#lambda1.
    def visitLambda1(self, ctx:IonaParser.Lambda1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#lambda2.
    def visitLambda2(self, ctx:IonaParser.Lambda2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#add2.
    def visitAdd2(self, ctx:IonaParser.Add2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#add1.
    def visitAdd1(self, ctx:IonaParser.Add1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#mul2.
    def visitMul2(self, ctx:IonaParser.Mul2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#mul1.
    def visitMul1(self, ctx:IonaParser.Mul1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#app2.
    def visitApp2(self, ctx:IonaParser.App2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#app1.
    def visitApp1(self, ctx:IonaParser.App1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#primary1.
    def visitPrimary1(self, ctx:IonaParser.Primary1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#primary2.
    def visitPrimary2(self, ctx:IonaParser.Primary2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#primary3.
    def visitPrimary3(self, ctx:IonaParser.Primary3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#primary4.
    def visitPrimary4(self, ctx:IonaParser.Primary4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#matchExpr.
    def visitMatchExpr(self, ctx:IonaParser.MatchExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#matchCase.
    def visitMatchCase(self, ctx:IonaParser.MatchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IonaParser#letExpr.
    def visitLetExpr(self, ctx:IonaParser.LetExprContext):
        return self.visitChildren(ctx)



del IonaParser