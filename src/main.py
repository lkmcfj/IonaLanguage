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

struct _DataCtorCurryBase {
    static void display() {
        std::cout << "A (maybe curried) data constructor\\n";
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
    results = []
    for t in trees:
        ret = t.gen([], alloc, f)
        if ret is not None:
            results.append(ret)
    f.write('int main() {\n')
    for result in results:
        f.write('    {\n')
        f.write('        using result = {};\n'.format(result))
        f.write('        result::display();\n    }\n')
    f.write('}')