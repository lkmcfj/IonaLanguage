
#include <iostream>
#include <typeinfo>

template <int v>
struct _Int {
    static constexpr int value = v;

    static void display() {
        std::cout << v << '\n';
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
        std::cout << "An abstraction\n";
    }
};

struct _MatchBase {
    static void display() {
        std::cout << "A pattern match\n";
    }
};

struct _DataCtorCurryBase {
    static void display() {
        std::cout << "A (maybe curried) data constructor\n";
    }
};
struct True {
    static void display() {
        std::cout << "A value from data constructor True\n";
    }
};

struct False {
    static void display() {
        std::cout << "A value from data constructor False\n";
    }
};

struct Empty {
    static void display() {
        std::cout << "A value from data constructor Empty\n";
    }
};

template <class _param0, class _param1>
struct List {
    static void display() {
        std::cout << "A value from data constructor List\n";
    }
};
template <class _param0>
struct _List_Curry1 : _DataCtorCurryBase {
    template <class _param1>
    using apply = List<_param0, _param1>;
};
struct _List_Curry0 : _DataCtorCurryBase {
    template <class _param0>
    using apply = _List_Curry1<_param0>;
};

struct _Abs0 : _AbsBase {
    template <class f>
    using apply = f;
};

struct _Abs1 : _AbsBase {
    template <class x>
    using apply = x;
};

struct _Abs2 : _AbsBase {
    template <class f>
    using apply = typename f::template apply<typename _IntMul<_Int<23>, _Int<34>>::result>;
};

struct _Abs3 : _AbsBase {
    template <class x>
    using apply = typename _IntDiv<x, _Int<2>>::result;
};

int main() {
    {
        using result = True;
        result::display();
    }
    {
        using result = typename _List_Curry0::template apply<True>::template apply<typename _List_Curry0::template apply<False>::template apply<Empty>>;
        result::display();
    }
    {
        using result = typename _IntAdd<_Int<3>, _Int<4>>::result;
        result::display();
    }
    {
        using result = typename _List_Curry0::template apply<False>;
        result::display();
    }
    {
        using result = _List_Curry0;
        result::display();
    }
    {
        using result = typename _Abs0::template apply<_Abs1>;
        result::display();
    }
    {
        using result = typename _Abs2::template apply<_Abs3>;
        result::display();
    }
}