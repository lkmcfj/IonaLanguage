# Generated from Iona.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,40,8,1,10,
        1,12,1,43,9,1,1,1,1,1,1,2,4,2,48,8,2,11,2,12,2,49,1,3,1,3,1,3,3,
        3,55,8,3,1,4,1,4,1,4,1,4,1,4,3,4,62,8,4,1,5,1,5,1,5,1,5,1,5,1,5,
        5,5,70,8,5,10,5,12,5,73,9,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,81,8,6,10,
        6,12,6,84,9,6,1,7,1,7,1,7,1,7,1,7,5,7,91,8,7,10,7,12,7,94,9,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,103,8,8,1,9,1,9,1,9,1,9,4,9,109,8,
        9,11,9,12,9,110,1,10,1,10,1,10,5,10,116,8,10,10,10,12,10,119,9,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,0,3,10,12,
        14,12,0,2,4,6,8,10,12,14,16,18,20,22,0,2,1,0,3,4,1,0,5,6,132,0,27,
        1,0,0,0,2,33,1,0,0,0,4,47,1,0,0,0,6,54,1,0,0,0,8,61,1,0,0,0,10,63,
        1,0,0,0,12,74,1,0,0,0,14,85,1,0,0,0,16,102,1,0,0,0,18,104,1,0,0,
        0,20,112,1,0,0,0,22,123,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,
        30,31,3,6,3,0,31,32,5,0,0,1,32,1,1,0,0,0,33,34,5,1,0,0,34,35,5,20,
        0,0,35,36,5,16,0,0,36,41,3,4,2,0,37,38,5,17,0,0,38,40,3,4,2,0,39,
        37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,
        0,43,41,1,0,0,0,44,45,5,15,0,0,45,3,1,0,0,0,46,48,5,20,0,0,47,46,
        1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,
        55,3,8,4,0,52,55,3,18,9,0,53,55,3,22,11,0,54,51,1,0,0,0,54,52,1,
        0,0,0,54,53,1,0,0,0,55,7,1,0,0,0,56,57,5,13,0,0,57,58,5,19,0,0,58,
        59,5,2,0,0,59,62,3,8,4,0,60,62,3,10,5,0,61,56,1,0,0,0,61,60,1,0,
        0,0,62,9,1,0,0,0,63,64,6,5,-1,0,64,65,3,12,6,0,65,71,1,0,0,0,66,
        67,10,2,0,0,67,68,7,0,0,0,68,70,3,12,6,0,69,66,1,0,0,0,70,73,1,0,
        0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,11,1,0,0,0,73,71,1,0,0,0,74,75,
        6,6,-1,0,75,76,3,14,7,0,76,82,1,0,0,0,77,78,10,2,0,0,78,79,7,1,0,
        0,79,81,3,14,7,0,80,77,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,
        1,0,0,0,83,13,1,0,0,0,84,82,1,0,0,0,85,86,6,7,-1,0,86,87,3,16,8,
        0,87,92,1,0,0,0,88,89,10,2,0,0,89,91,3,16,8,0,90,88,1,0,0,0,91,94,
        1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,15,1,0,0,0,94,92,1,0,0,0,
        95,103,5,18,0,0,96,103,5,19,0,0,97,98,5,11,0,0,98,99,3,6,3,0,99,
        100,5,12,0,0,100,103,1,0,0,0,101,103,5,20,0,0,102,95,1,0,0,0,102,
        96,1,0,0,0,102,97,1,0,0,0,102,101,1,0,0,0,103,17,1,0,0,0,104,105,
        5,7,0,0,105,106,3,6,3,0,106,108,5,8,0,0,107,109,3,20,10,0,108,107,
        1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,19,1,
        0,0,0,112,113,5,17,0,0,113,117,5,20,0,0,114,116,5,19,0,0,115,114,
        1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,
        1,0,0,0,119,117,1,0,0,0,120,121,5,2,0,0,121,122,3,6,3,0,122,21,1,
        0,0,0,123,124,5,9,0,0,124,125,5,19,0,0,125,126,5,16,0,0,126,127,
        3,6,3,0,127,128,5,10,0,0,128,129,3,6,3,0,129,23,1,0,0,0,11,27,41,
        49,54,61,71,82,92,102,110,117
    ]

class IonaParser ( Parser ):

    grammarFileName = "Iona.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'data'", "'->'", "'+'", "'-'", "'*'", 
                     "'/'", "'match'", "'with'", "'let'", "'in'", "'('", 
                     "')'", "'\\'", "'.'", "';'", "'='", "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Lparen", "Rparen", 
                      "Lambda", "Dot", "Semicolon", "Equal", "Bar", "IntLiteral", 
                      "LowerIdentifier", "UpperIdentifier", "WS" ]

    RULE_program = 0
    RULE_dataDecl = 1
    RULE_dataDeclPart = 2
    RULE_expr = 3
    RULE_lambdaExpr = 4
    RULE_addExpr = 5
    RULE_mulExpr = 6
    RULE_appExpr = 7
    RULE_primaryExpr = 8
    RULE_matchExpr = 9
    RULE_matchCase = 10
    RULE_letExpr = 11

    ruleNames =  [ "program", "dataDecl", "dataDeclPart", "expr", "lambdaExpr", 
                   "addExpr", "mulExpr", "appExpr", "primaryExpr", "matchExpr", 
                   "matchCase", "letExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    Lparen=11
    Rparen=12
    Lambda=13
    Dot=14
    Semicolon=15
    Equal=16
    Bar=17
    IntLiteral=18
    LowerIdentifier=19
    UpperIdentifier=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(IonaParser.ExprContext,0)


        def EOF(self):
            return self.getToken(IonaParser.EOF, 0)

        def dataDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IonaParser.DataDeclContext)
            else:
                return self.getTypedRuleContext(IonaParser.DataDeclContext,i)


        def getRuleIndex(self):
            return IonaParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = IonaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 24
                self.dataDecl()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.expr()
            self.state = 31
            self.match(IonaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UpperIdentifier(self):
            return self.getToken(IonaParser.UpperIdentifier, 0)

        def Equal(self):
            return self.getToken(IonaParser.Equal, 0)

        def dataDeclPart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IonaParser.DataDeclPartContext)
            else:
                return self.getTypedRuleContext(IonaParser.DataDeclPartContext,i)


        def Semicolon(self):
            return self.getToken(IonaParser.Semicolon, 0)

        def Bar(self, i:int=None):
            if i is None:
                return self.getTokens(IonaParser.Bar)
            else:
                return self.getToken(IonaParser.Bar, i)

        def getRuleIndex(self):
            return IonaParser.RULE_dataDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataDecl" ):
                return visitor.visitDataDecl(self)
            else:
                return visitor.visitChildren(self)




    def dataDecl(self):

        localctx = IonaParser.DataDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dataDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(IonaParser.T__0)
            self.state = 34
            self.match(IonaParser.UpperIdentifier)
            self.state = 35
            self.match(IonaParser.Equal)
            self.state = 36
            self.dataDeclPart()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 37
                self.match(IonaParser.Bar)
                self.state = 38
                self.dataDeclPart()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(IonaParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataDeclPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UpperIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(IonaParser.UpperIdentifier)
            else:
                return self.getToken(IonaParser.UpperIdentifier, i)

        def getRuleIndex(self):
            return IonaParser.RULE_dataDeclPart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataDeclPart" ):
                return visitor.visitDataDeclPart(self)
            else:
                return visitor.visitChildren(self)




    def dataDeclPart(self):

        localctx = IonaParser.DataDeclPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dataDeclPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.match(IonaParser.UpperIdentifier)
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IonaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Expr3Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def letExpr(self):
            return self.getTypedRuleContext(IonaParser.LetExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)


    class Expr2Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matchExpr(self):
            return self.getTypedRuleContext(IonaParser.MatchExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)


    class Expr1Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lambdaExpr(self):
            return self.getTypedRuleContext(IonaParser.LambdaExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = IonaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 13, 18, 19, 20]:
                localctx = IonaParser.Expr1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.lambdaExpr()
                pass
            elif token in [7]:
                localctx = IonaParser.Expr2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.matchExpr()
                pass
            elif token in [9]:
                localctx = IonaParser.Expr3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.letExpr()
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


    class LambdaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IonaParser.RULE_lambdaExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Lambda2Context(LambdaExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.LambdaExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addExpr(self):
            return self.getTypedRuleContext(IonaParser.AddExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambda2" ):
                return visitor.visitLambda2(self)
            else:
                return visitor.visitChildren(self)


    class Lambda1Context(LambdaExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.LambdaExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Lambda(self):
            return self.getToken(IonaParser.Lambda, 0)
        def LowerIdentifier(self):
            return self.getToken(IonaParser.LowerIdentifier, 0)
        def lambdaExpr(self):
            return self.getTypedRuleContext(IonaParser.LambdaExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambda1" ):
                return visitor.visitLambda1(self)
            else:
                return visitor.visitChildren(self)



    def lambdaExpr(self):

        localctx = IonaParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lambdaExpr)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = IonaParser.Lambda1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(IonaParser.Lambda)
                self.state = 57
                self.match(IonaParser.LowerIdentifier)
                self.state = 58
                self.match(IonaParser.T__1)
                self.state = 59
                self.lambdaExpr()
                pass
            elif token in [11, 18, 19, 20]:
                localctx = IonaParser.Lambda2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.addExpr(0)
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


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IonaParser.RULE_addExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Add2Context(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.AddExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(IonaParser.MulExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd2" ):
                return visitor.visitAdd2(self)
            else:
                return visitor.visitChildren(self)


    class Add1Context(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.AddExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addExpr(self):
            return self.getTypedRuleContext(IonaParser.AddExprContext,0)

        def mulExpr(self):
            return self.getTypedRuleContext(IonaParser.MulExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd1" ):
                return visitor.visitAdd1(self)
            else:
                return visitor.visitChildren(self)



    def addExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IonaParser.AddExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_addExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = IonaParser.Add2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 64
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IonaParser.Add1Context(self, IonaParser.AddExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                    self.state = 66
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 67
                    _la = self._input.LA(1)
                    if not(_la==3 or _la==4):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 68
                    self.mulExpr(0) 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IonaParser.RULE_mulExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Mul2Context(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def appExpr(self):
            return self.getTypedRuleContext(IonaParser.AppExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul2" ):
                return visitor.visitMul2(self)
            else:
                return visitor.visitChildren(self)


    class Mul1Context(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(IonaParser.MulExprContext,0)

        def appExpr(self):
            return self.getTypedRuleContext(IonaParser.AppExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul1" ):
                return visitor.visitMul1(self)
            else:
                return visitor.visitChildren(self)



    def mulExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IonaParser.MulExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_mulExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = IonaParser.Mul2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 75
            self.appExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IonaParser.Mul1Context(self, IonaParser.MulExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                    self.state = 77
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 78
                    _la = self._input.LA(1)
                    if not(_la==5 or _la==6):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 79
                    self.appExpr(0) 
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AppExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IonaParser.RULE_appExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class App2Context(AppExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.AppExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primaryExpr(self):
            return self.getTypedRuleContext(IonaParser.PrimaryExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApp2" ):
                return visitor.visitApp2(self)
            else:
                return visitor.visitChildren(self)


    class App1Context(AppExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.AppExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def appExpr(self):
            return self.getTypedRuleContext(IonaParser.AppExprContext,0)

        def primaryExpr(self):
            return self.getTypedRuleContext(IonaParser.PrimaryExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApp1" ):
                return visitor.visitApp1(self)
            else:
                return visitor.visitChildren(self)



    def appExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IonaParser.AppExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_appExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = IonaParser.App2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 86
            self.primaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IonaParser.App1Context(self, IonaParser.AppExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_appExpr)
                    self.state = 88
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 89
                    self.primaryExpr() 
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IonaParser.RULE_primaryExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Primary2Context(PrimaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.PrimaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LowerIdentifier(self):
            return self.getToken(IonaParser.LowerIdentifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary2" ):
                return visitor.visitPrimary2(self)
            else:
                return visitor.visitChildren(self)


    class Primary3Context(PrimaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.PrimaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Lparen(self):
            return self.getToken(IonaParser.Lparen, 0)
        def expr(self):
            return self.getTypedRuleContext(IonaParser.ExprContext,0)

        def Rparen(self):
            return self.getToken(IonaParser.Rparen, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary3" ):
                return visitor.visitPrimary3(self)
            else:
                return visitor.visitChildren(self)


    class Primary4Context(PrimaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.PrimaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UpperIdentifier(self):
            return self.getToken(IonaParser.UpperIdentifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary4" ):
                return visitor.visitPrimary4(self)
            else:
                return visitor.visitChildren(self)


    class Primary1Context(PrimaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IonaParser.PrimaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IntLiteral(self):
            return self.getToken(IonaParser.IntLiteral, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary1" ):
                return visitor.visitPrimary1(self)
            else:
                return visitor.visitChildren(self)



    def primaryExpr(self):

        localctx = IonaParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primaryExpr)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = IonaParser.Primary1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(IonaParser.IntLiteral)
                pass
            elif token in [19]:
                localctx = IonaParser.Primary2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(IonaParser.LowerIdentifier)
                pass
            elif token in [11]:
                localctx = IonaParser.Primary3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(IonaParser.Lparen)
                self.state = 98
                self.expr()
                self.state = 99
                self.match(IonaParser.Rparen)
                pass
            elif token in [20]:
                localctx = IonaParser.Primary4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.match(IonaParser.UpperIdentifier)
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


    class MatchExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(IonaParser.ExprContext,0)


        def matchCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IonaParser.MatchCaseContext)
            else:
                return self.getTypedRuleContext(IonaParser.MatchCaseContext,i)


        def getRuleIndex(self):
            return IonaParser.RULE_matchExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchExpr" ):
                return visitor.visitMatchExpr(self)
            else:
                return visitor.visitChildren(self)




    def matchExpr(self):

        localctx = IonaParser.MatchExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_matchExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(IonaParser.T__6)
            self.state = 105
            self.expr()
            self.state = 106
            self.match(IonaParser.T__7)
            self.state = 108 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 107
                    self.matchCase()

                else:
                    raise NoViableAltException(self)
                self.state = 110 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Bar(self):
            return self.getToken(IonaParser.Bar, 0)

        def UpperIdentifier(self):
            return self.getToken(IonaParser.UpperIdentifier, 0)

        def expr(self):
            return self.getTypedRuleContext(IonaParser.ExprContext,0)


        def LowerIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(IonaParser.LowerIdentifier)
            else:
                return self.getToken(IonaParser.LowerIdentifier, i)

        def getRuleIndex(self):
            return IonaParser.RULE_matchCase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchCase" ):
                return visitor.visitMatchCase(self)
            else:
                return visitor.visitChildren(self)




    def matchCase(self):

        localctx = IonaParser.MatchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_matchCase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(IonaParser.Bar)
            self.state = 113
            self.match(IonaParser.UpperIdentifier)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 114
                self.match(IonaParser.LowerIdentifier)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(IonaParser.T__1)
            self.state = 121
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LowerIdentifier(self):
            return self.getToken(IonaParser.LowerIdentifier, 0)

        def Equal(self):
            return self.getToken(IonaParser.Equal, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IonaParser.ExprContext)
            else:
                return self.getTypedRuleContext(IonaParser.ExprContext,i)


        def getRuleIndex(self):
            return IonaParser.RULE_letExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetExpr" ):
                return visitor.visitLetExpr(self)
            else:
                return visitor.visitChildren(self)




    def letExpr(self):

        localctx = IonaParser.LetExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_letExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(IonaParser.T__8)
            self.state = 124
            self.match(IonaParser.LowerIdentifier)
            self.state = 125
            self.match(IonaParser.Equal)
            self.state = 126
            self.expr()
            self.state = 127
            self.match(IonaParser.T__9)
            self.state = 128
            self.expr()
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
        self._predicates[5] = self.addExpr_sempred
        self._predicates[6] = self.mulExpr_sempred
        self._predicates[7] = self.appExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def addExpr_sempred(self, localctx:AddExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def mulExpr_sempred(self, localctx:MulExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def appExpr_sempred(self, localctx:AppExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




