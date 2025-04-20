
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
template <class x, class y>
struct _Abs0 : _AbsBase {
    template <class z>
    using apply = typename x::template apply<y>::template apply<z>;
};

template <class x>
struct _Abs1 : _AbsBase {
    template <class y>
    using apply = _Abs0<x, y>;
};

struct _Abs2 : _AbsBase {
    template <class x>
    using apply = _Abs1<x>;
};

template <class x>
struct _Abs3 : _AbsBase {
    template <class y>
    using apply = typename _IntAdd<_Int<1>, typename x::template apply<y>>::result;
};

struct _Abs4 : _AbsBase {
    template <class x>
    using apply = _Abs3<x>;
};

struct _Abs5 : _AbsBase {
    template <class x>
    using apply = typename _IntMul<_Int<3>, x>::result;
};

int main() {
    {
        using result = typename _Abs2::template apply<_Abs4>::template apply<_Abs5>::template apply<_Int<234>>;
        result::display();
    }
}