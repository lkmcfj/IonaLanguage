# Generated from Iona.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,21,117,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,
        1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,
        1,14,1,15,1,15,1,16,1,16,1,17,3,17,93,8,17,1,17,4,17,96,8,17,11,
        17,12,17,97,1,18,1,18,5,18,102,8,18,10,18,12,18,105,9,18,1,19,1,
        19,5,19,109,8,19,10,19,12,19,112,9,19,1,20,1,20,1,20,1,20,0,0,21,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,1,0,5,1,0,48,57,
        1,0,97,122,3,0,48,57,65,90,97,122,1,0,65,90,3,0,9,10,13,13,32,32,
        120,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,
        0,41,1,0,0,0,1,43,1,0,0,0,3,48,1,0,0,0,5,51,1,0,0,0,7,53,1,0,0,0,
        9,55,1,0,0,0,11,57,1,0,0,0,13,59,1,0,0,0,15,65,1,0,0,0,17,70,1,0,
        0,0,19,74,1,0,0,0,21,77,1,0,0,0,23,79,1,0,0,0,25,81,1,0,0,0,27,83,
        1,0,0,0,29,85,1,0,0,0,31,87,1,0,0,0,33,89,1,0,0,0,35,92,1,0,0,0,
        37,99,1,0,0,0,39,106,1,0,0,0,41,113,1,0,0,0,43,44,5,100,0,0,44,45,
        5,97,0,0,45,46,5,116,0,0,46,47,5,97,0,0,47,2,1,0,0,0,48,49,5,45,
        0,0,49,50,5,62,0,0,50,4,1,0,0,0,51,52,5,43,0,0,52,6,1,0,0,0,53,54,
        5,45,0,0,54,8,1,0,0,0,55,56,5,42,0,0,56,10,1,0,0,0,57,58,5,47,0,
        0,58,12,1,0,0,0,59,60,5,109,0,0,60,61,5,97,0,0,61,62,5,116,0,0,62,
        63,5,99,0,0,63,64,5,104,0,0,64,14,1,0,0,0,65,66,5,119,0,0,66,67,
        5,105,0,0,67,68,5,116,0,0,68,69,5,104,0,0,69,16,1,0,0,0,70,71,5,
        108,0,0,71,72,5,101,0,0,72,73,5,116,0,0,73,18,1,0,0,0,74,75,5,105,
        0,0,75,76,5,110,0,0,76,20,1,0,0,0,77,78,5,40,0,0,78,22,1,0,0,0,79,
        80,5,41,0,0,80,24,1,0,0,0,81,82,5,92,0,0,82,26,1,0,0,0,83,84,5,46,
        0,0,84,28,1,0,0,0,85,86,5,59,0,0,86,30,1,0,0,0,87,88,5,61,0,0,88,
        32,1,0,0,0,89,90,5,124,0,0,90,34,1,0,0,0,91,93,5,45,0,0,92,91,1,
        0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,96,7,0,0,0,95,94,1,0,0,0,96,
        97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,36,1,0,0,0,99,103,7,1,
        0,0,100,102,7,2,0,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,
        0,0,103,104,1,0,0,0,104,38,1,0,0,0,105,103,1,0,0,0,106,110,7,3,0,
        0,107,109,7,2,0,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,
        0,110,111,1,0,0,0,111,40,1,0,0,0,112,110,1,0,0,0,113,114,7,4,0,0,
        114,115,1,0,0,0,115,116,6,20,0,0,116,42,1,0,0,0,5,0,92,97,103,110,
        1,6,0,0
    ]

class IonaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    Lparen = 11
    Rparen = 12
    Lambda = 13
    Dot = 14
    Semicolon = 15
    Equal = 16
    Bar = 17
    IntLiteral = 18
    LowerIdentifier = 19
    UpperIdentifier = 20
    WS = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'data'", "'->'", "'+'", "'-'", "'*'", "'/'", "'match'", "'with'", 
            "'let'", "'in'", "'('", "')'", "'\\'", "'.'", "';'", "'='", 
            "'|'" ]

    symbolicNames = [ "<INVALID>",
            "Lparen", "Rparen", "Lambda", "Dot", "Semicolon", "Equal", "Bar", 
            "IntLiteral", "LowerIdentifier", "UpperIdentifier", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "Lparen", "Rparen", "Lambda", 
                  "Dot", "Semicolon", "Equal", "Bar", "IntLiteral", "LowerIdentifier", 
                  "UpperIdentifier", "WS" ]

    grammarFileName = "Iona.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


