import sys
from antlr4 import *
from parsing.IonaParser import IonaParser
from parsing.IonaLexer import IonaLexer
from visitor import ExtractAST
from utils import Allocator

RUNTIME = '''
#include <iostream>
#include <typeinfo>

template <int v>
struct _Int {
    static constexpr int value = v;

    static void display() {
        std::cout << v << '\\n';
    }
};

template <class L, class R>
struct _IntAdd {};
template <int l, int r>
struct _IntAdd<_Int<l>, _Int<r>> {
    using result = _Int<l + r>;
};

template <class L, class R>
struct _IntMinus {};
template <int l, int r>
struct _IntMinus<_Int<l>, _Int<r>> {
    using result = _Int<l - r>;
};

template <class L, class R>
struct _IntMul {};
template <int l, int r>
struct _IntMul<_Int<l>, _Int<r>> {
    using result = _Int<l * r>;
};

template <class L, class R>
struct _IntDiv {};
template <int l, int r>
struct _IntDiv<_Int<l>, _Int<r>> {
    using result = _Int<l / r>;
};

struct _AbsBase {
    static void display() {
        std::cout << "An abstraction\\n";
    }
};

struct _MatchBase {
    static void display() {
        std::cout << "A pattern match\\n";
    }
};
'''

stream = FileStream(sys.argv[1])
lexer = IonaLexer(stream)
tokens = CommonTokenStream(lexer)
parser = IonaParser(tokens)
root = parser.program()
visitor = ExtractAST()
trees = root.accept(visitor)
alloc = Allocator()
with open(sys.argv[2], 'w') as f:
    f.write(RUNTIME)
    for t in trees[:-1]:
        t.gen([], alloc, f)
    result = trees[-1].gen([], alloc, f)
    f.write('int main() {\n')
    f.write("    {}::display();\n".format(result))
    f.write('}')