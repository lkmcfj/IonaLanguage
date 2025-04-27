## 1. Project Summary

This project compiles a simple functional language, IonaLanguage, into C++ template metaprogramming. The source code of IonaLanguage consists of several data type definitions and lambda expressions, each ending with a semicolon. The generated C++ code should be compiled with a C++17-compliant compiler. The resulting executable prints the outcomes of the expressions, one per line.

The evaluation of the expressions is performed through a series of template instantiations in C++, which happens at the compile time of the C++ code. Therefore, The C++ compiler gives a "template instantiation depth exceeded" error for infinite reduction, and a template instantiation error when the semantics "gets stuck".

In the `examples/` directory, a list of source code and respective generated C++ code is given. The language is basically untyped lambda calculus with let bindings, primitive integers, algebraic data types and pattern matching. Please refer to the examples or `src/parsing/Iona.g4` for syntax. Example 5 is an example for infinite reduction. Example 6 is an example for "getting stuck".

This is a course project for CS 642 at the University of Waterloo.

## 2. Usage

This project is implemented in Python 3. The only dependency is `antlr4-python3-runtime 4.13.2`.

For compiling an IonaLanguage source file to C++ code:

```
$ python src/main.py <input file path> <output file path>
```
