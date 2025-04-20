
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
template <class f, class x, class head, class tail, class cons, class zero, class two, class succ>
struct _Abs0 : _AbsBase {
    template <class pred>
    using apply = typename pred::template apply<two>;
};

template <class f, class x, class head, class tail, class cons, class zero, class two, class succ, class n>
struct _Abs1 : _AbsBase {
    template <class p>
    using apply = typename cons::template apply<typename succ::template apply<typename head::template apply<p>>>::template apply<typename head::template apply<p>>;
};

template <class f, class x, class head, class tail, class cons, class zero, class two, class succ>
struct _Abs2 : _AbsBase {
    template <class n>
    using apply = typename tail::template apply<typename n::template apply<_Abs1<f, x, head, tail, cons, zero, two, succ, n>>::template apply<typename cons::template apply<zero>::template apply<zero>>>;
};

template <class f, class x, class head, class tail, class cons, class zero, class two>
struct _Abs3 : _AbsBase {
    template <class succ>
    using apply = typename _Abs0<f, x, head, tail, cons, zero, two, succ>::template apply<_Abs2<f, x, head, tail, cons, zero, two, succ>>;
};

template <class f, class x, class head, class tail, class cons, class zero, class two, class n, class _fresh0>
struct _Abs4 : _AbsBase {
    template <class _fresh1>
    using apply = typename n::template apply<_fresh0>::template apply<typename _fresh0::template apply<_fresh1>>;
};

template <class f, class x, class head, class tail, class cons, class zero, class two, class n>
struct _Abs5 : _AbsBase {
    template <class _fresh0>
    using apply = _Abs4<f, x, head, tail, cons, zero, two, n, _fresh0>;
};

template <class f, class x, class head, class tail, class cons, class zero, class two>
struct _Abs6 : _AbsBase {
    template <class n>
    using apply = _Abs5<f, x, head, tail, cons, zero, two, n>;
};

template <class f, class x, class head, class tail, class cons, class zero>
struct _Abs7 : _AbsBase {
    template <class two>
    using apply = typename _Abs3<f, x, head, tail, cons, zero, two>::template apply<_Abs6<f, x, head, tail, cons, zero, two>>;
};

template <class f, class x, class head, class tail, class cons>
struct _Abs8 : _AbsBase {
    template <class zero>
    using apply = _Abs7<f, x, head, tail, cons, zero>;
};

template <class f, class x, class head, class tail>
struct _Abs9 : _AbsBase {
    template <class cons>
    using apply = _Abs8<f, x, head, tail, cons>;
};

template <class f, class x, class head>
struct _Abs10 : _AbsBase {
    template <class tail>
    using apply = _Abs9<f, x, head, tail>;
};

template <class f, class x>
struct _Abs11 : _AbsBase {
    template <class head>
    using apply = _Abs10<f, x, head>;
};

template <class f, class x, class l, class _fresh2>
struct _Abs12 : _AbsBase {
    template <class y>
    using apply = _fresh2;
};

template <class f, class x, class l>
struct _Abs13 : _AbsBase {
    template <class _fresh2>
    using apply = _Abs12<f, x, l, _fresh2>;
};

template <class f, class x>
struct _Abs14 : _AbsBase {
    template <class l>
    using apply = typename l::template apply<_Abs13<f, x, l>>;
};

template <class f, class x, class l, class _fresh3>
struct _Abs15 : _AbsBase {
    template <class y>
    using apply = y;
};

template <class f, class x, class l>
struct _Abs16 : _AbsBase {
    template <class _fresh3>
    using apply = _Abs15<f, x, l, _fresh3>;
};

template <class f, class x>
struct _Abs17 : _AbsBase {
    template <class l>
    using apply = typename l::template apply<_Abs16<f, x, l>>;
};

template <class f, class x, class h, class t>
struct _Abs18 : _AbsBase {
    template <class s>
    using apply = typename s::template apply<h>::template apply<t>;
};

template <class f, class x, class h>
struct _Abs19 : _AbsBase {
    template <class t>
    using apply = _Abs18<f, x, h, t>;
};

template <class f, class x>
struct _Abs20 : _AbsBase {
    template <class h>
    using apply = _Abs19<f, x, h>;
};

template <class f, class x, class _fresh4>
struct _Abs21 : _AbsBase {
    template <class _fresh5>
    using apply = _fresh5;
};

template <class f, class x>
struct _Abs22 : _AbsBase {
    template <class _fresh4>
    using apply = _Abs21<f, x, _fresh4>;
};

template <class f, class x, class _fresh6>
struct _Abs23 : _AbsBase {
    template <class _fresh7>
    using apply = typename _fresh6::template apply<typename _fresh6::template apply<_fresh7>>;
};

template <class f, class x>
struct _Abs24 : _AbsBase {
    template <class _fresh6>
    using apply = _Abs23<f, x, _fresh6>;
};

template <class f>
struct _Abs25 : _AbsBase {
    template <class x>
    using apply = typename _Abs11<f, x>::template apply<_Abs14<f, x>>::template apply<_Abs17<f, x>>::template apply<_Abs20<f, x>>::template apply<_Abs22<f, x>>::template apply<_Abs24<f, x>>::template apply<f>::template apply<x>;
};

struct _Abs26 : _AbsBase {
    template <class f>
    using apply = typename _Abs25<f>::template apply<_Int<233>>;
};

struct _Abs27 : _AbsBase {
    template <class x>
    using apply = typename _IntAdd<x, _Int<1>>::result;
};

int main() {
    {
        using result = typename _Abs26::template apply<_Abs27>;
        result::display();
    }
}