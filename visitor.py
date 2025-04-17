import sys
from parsing.IonaVisitor import IonaVisitor
from parsing.IonaParser import IonaParser
import tree

class ExtractAST(IonaVisitor):

    def __init__(self):
        super().__init__()
        self.fresh_count = 0
        self.var_mapping = {}
        self.existing_data_ctors = set()
    
    def add_to_mapping(self, var_name):
        if var_name in self.var_mapping:
            self.var_mapping[var_name] = '_fresh{}'.format(self.fresh_count)
            self.fresh_count = self.fresh_count + 1
        else:
            self.var_mapping[var_name] = var_name
        return self.var_mapping[var_name]

    def visitProgram(self, ctx:IonaParser.ProgramContext):
        ret = []
        for data_decl in ctx.dataDecl():
            ret.extend(data_decl.accept(self))
        ret.append(ctx.expr().accept(self))
        return ret

    def visitDataDecl(self, ctx:IonaParser.DataDeclContext):
        return [child.accept(self) for child in ctx.dataDeclPart()]
    
    def visitDataDeclPart(self, ctx:IonaParser.DataDeclPartContext):
        names = [child.getText() for child in ctx.UpperIdentifier()]
        ctor_name = names[0]
        if ctor_name in self.existing_data_ctors:
            print('Duplicate data constructor:', ctor_name)
            sys.exit(1)
        self.existing_data_ctors.add(ctor_name)
        return tree.DataConstructorDecl(ctor_name, len(names) - 1)

    def visitExpr1(self, ctx:IonaParser.Expr1Context):
        return ctx.lambdaExpr().accept(self)

    def visitExpr2(self, ctx:IonaParser.Expr2Context):
        return ctx.matchExpr().accept(self)

    def visitExpr3(self, ctx:IonaParser.Expr3Context):
        return ctx.letExpr().accept(self)
    
    def visitLambda1(self, ctx:IonaParser.Lambda1Context):
        name = ctx.LowerIdentifier().getText()
        old_mapping = self.var_mapping.copy()
        name = self.add_to_mapping(name)
        body = ctx.lambdaExpr().accept(self)
        ret = tree.Abstraction(name, body)
        self.var_mapping = old_mapping
        return ret
    
    def visitLambda2(self, ctx:IonaParser.Lambda2Context):
        return ctx.addExpr().accept(self)
    
    def visitAdd2(self, ctx:IonaParser.Add2Context):
        return ctx.mulExpr().accept(self)
    
    def visitAdd1(self, ctx:IonaParser.Add1Context):
        lhs = ctx.addExpr().accept(self)
        rhs = ctx.mulExpr().accept(self)
        return tree.BinaryOperation(ctx.children[1].getText(), lhs, rhs)

    def visitMul2(self, ctx:IonaParser.Mul2Context):
        return ctx.appExpr().accept(self)
    
    def visitMul1(self, ctx:IonaParser.Mul1Context):
        lhs = ctx.mulExpr().accept(self)
        rhs = ctx.appExpr().accept(self)
        return tree.BinaryOperation(ctx.children[1].getText(), lhs, rhs)

    def visitApp2(self, ctx:IonaParser.App2Context):
        return ctx.primaryExpr().accept(self)
    
    def visitApp1(self, ctx:IonaParser.App1Context):
        rator = ctx.appExpr().accept(self)
        rand = ctx.primaryExpr().accept(self)
        return tree.Application(rator, rand)
    
    def visitPrimary1(self, ctx:IonaParser.Primary1Context):
        return tree.IntLiteral(int(ctx.IntLiteral().getText()))
    
    def visitPrimary2(self, ctx:IonaParser.Primary2Context):
        return tree.Var(self.var_mapping[ctx.LowerIdentifier().getText()])
    
    def visitPrimary3(self, ctx:IonaParser.Primary3Context):
        return ctx.expr().accept(self)
    
    def visitPrimary4(self, ctx:IonaParser.Primary4Context):
        data_ctor = ctx.UpperIdentifier().getText()
        if data_ctor not in self.existing_data_ctors:
            print('Unrecognized data constructor:', data_ctor)
            sys.exit(1)
        return tree.DataConstructor(data_ctor)
    
    def visitMatchExpr(self, ctx:IonaParser.MatchExprContext):
        arg = ctx.expr().accept(self)
        cases = [c.accept(self) for c in ctx.matchCase()]
        return tree.PatternMatching(arg, cases)
    
    def visitMatchCase(self, ctx:IonaParser.MatchCaseContext):
        data_ctor = ctx.UpperIdentifier().getText()
        if data_ctor not in self.existing_data_ctors:
            print('Unrecognized data constructor:', data_ctor)
            sys.exit(1)
        old_mapping = self.var_mapping.copy()
        var_names = [ident.getText() for ident in ctx.LowerIdentifier()]
        var_names = [self.add_to_mapping(v) for v in var_names]
        ret = tree.PatternMatching.MatchCase(data_ctor, var_names, ctx.expr().accept(self))
        self.var_mapping = old_mapping
        return ret

    def visitLetExpr(self, ctx:IonaParser.LetExprContext):
        name = ctx.LowerIdentifier().getText()
        rhs = ctx.expr(0).accept(self)
        old_mapping = self.var_mapping.copy()
        name = self.add_to_mapping(name)
        body = ctx.expr(1).accept(self)
        self.var_mapping = old_mapping
        return tree.LetBinding(name, rhs, body)