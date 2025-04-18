
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
        std::cout << "A True\n";
    }
};

struct False {
    static void display() {
        std::cout << "A False\n";
    }
};

struct Empty {
    static void display() {
        std::cout << "A Empty\n";
    }
};

template <class _param0, class _param1>
struct List {
    static void display() {
        std::cout << "A List\n";
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

template <class x, class head, class rest, class _param>
struct _Match0 : _MatchBase {};

template <class x, class head, class rest>
struct _Match0<x, head, rest, True> : _MatchBase {
    using result = _Int<1>;
};

template <class x, class head, class rest>
struct _Match0<x, head, rest, False> : _MatchBase {
    using result = _Int<0>;
};

template <class x, class _param>
struct _Match1 : _MatchBase {};

template <class x>
struct _Match1<x, Empty> : _MatchBase {
    using result = _Int<0>;
};

template <class x, class head, class rest>
struct _Match1<x, List<head, rest>> : _MatchBase {
    using result = typename _IntAdd<typename _Match0<x, head, rest, head>::result, _Int<2>>::result;
};

struct _Abs0 : _AbsBase {
    template <class x>
    using apply = typename _Match1<x, x>::result;
};

template <class x, class head, class rest, class _param>
struct _Match2 : _MatchBase {};

template <class x, class head, class rest>
struct _Match2<x, head, rest, True> : _MatchBase {
    using result = _Int<1>;
};

template <class x, class head, class rest>
struct _Match2<x, head, rest, False> : _MatchBase {
    using result = _Int<0>;
};

template <class x, class _param>
struct _Match3 : _MatchBase {};

template <class x>
struct _Match3<x, Empty> : _MatchBase {
    using result = _Int<0>;
};

template <class x, class head, class rest>
struct _Match3<x, List<head, rest>> : _MatchBase {
    using result = typename _IntAdd<typename _Match2<x, head, rest, head>::result, _Int<2>>::result;
};

struct _Abs1 : _AbsBase {
    template <class x>
    using apply = typename _Match3<x, x>::result;
};

template <class x, class head, class rest, class _param>
struct _Match4 : _MatchBase {};

template <class x, class head, class rest>
struct _Match4<x, head, rest, True> : _MatchBase {
    using result = _Int<1>;
};

template <class x, class head, class rest>
struct _Match4<x, head, rest, False> : _MatchBase {
    using result = _Int<0>;
};

template <class x, class _param>
struct _Match5 : _MatchBase {};

template <class x>
struct _Match5<x, Empty> : _MatchBase {
    using result = _Int<0>;
};

template <class x, class head, class rest>
struct _Match5<x, List<head, rest>> : _MatchBase {
    using result = typename _IntAdd<typename _Match4<x, head, rest, head>::result, _Int<2>>::result;
};

struct _Abs2 : _AbsBase {
    template <class x>
    using apply = typename _Match5<x, x>::result;
};

template <class head, class rest, class _param>
struct _Match6 : _MatchBase {};

template <class head, class rest>
struct _Match6<head, rest, True> : _MatchBase {
    using result = _Int<1>;
};

template <class head, class rest>
struct _Match6<head, rest, False> : _MatchBase {
    using result = _Int<0>;
};

template <class _param>
struct _Match7 : _MatchBase {};

template <>
struct _Match7<Empty> : _MatchBase {
    using result = _Int<0>;
};

template <class head, class rest>
struct _Match7<List<head, rest>> : _MatchBase {
    using result = typename _IntAdd<typename _Match6<head, rest, head>::result, _Int<2>>::result;
};

template <class head, class rest, class _param>
struct _Match8 : _MatchBase {};

template <class head, class rest>
struct _Match8<head, rest, True> : _MatchBase {
    using result = _Int<1>;
};

template <class head, class rest>
struct _Match8<head, rest, False> : _MatchBase {
    using result = _Int<0>;
};

template <class _param>
struct _Match9 : _MatchBase {};

template <>
struct _Match9<Empty> : _MatchBase {
    using result = _Int<0>;
};

template <class head, class rest>
struct _Match9<List<head, rest>> : _MatchBase {
    using result = typename _IntAdd<typename _Match8<head, rest, head>::result, _Int<2>>::result;
};

template <class head, class rest, class _param>
struct _Match10 : _MatchBase {};

template <class head, class rest>
struct _Match10<head, rest, True> : _MatchBase {
    using result = _Int<1>;
};

template <class head, class rest>
struct _Match10<head, rest, False> : _MatchBase {
    using result = _Int<0>;
};

template <class _param>
struct _Match11 : _MatchBase {};

template <>
struct _Match11<Empty> : _MatchBase {
    using result = _Int<0>;
};

template <class head, class rest>
struct _Match11<List<head, rest>> : _MatchBase {
    using result = typename _IntAdd<typename _Match10<head, rest, head>::result, _Int<2>>::result;
};

int main() {
    {
        using result = _Abs0::apply<Empty>;
        result::display();
    }
    {
        using result = _Abs1::apply<_List_Curry0::apply<True>::apply<Empty>>;
        result::display();
    }
    {
        using result = _Abs2::apply<_List_Curry0::apply<False>::apply<Empty>>;
        result::display();
    }
    {
        using result = typename _Match7<Empty>::result;
        result::display();
    }
    {
        using result = typename _Match9<_List_Curry0::apply<True>::apply<Empty>>::result;
        result::display();
    }
    {
        using result = typename _Match11<_List_Curry0::apply<False>::apply<Empty>>::result;
        result::display();
    }
}