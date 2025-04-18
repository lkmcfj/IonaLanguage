// (^a. \x: (a->a)->(a->a). \y: a->a. \z: a. x y z) { int } (^a. \x: a->a. \y: a. + 1 (x y)) {int} (\x: int. * 3 x) 234

/*
#include <functional>
template <class T>
using F<T> = std::function<T>;

template <class a>
struct f3 {
  using Tx = F<F<a(a)>(F<a(a)>)>;
  using Ty = F<a(a)>;
  Tx x;
  Ty y;

  f3(Tx _x, Ty _y): x(_x), y(_y) {}
  a operator()(a z) {
    return x(y)(z);
  }
};

template <class a>
struct f2 {
    using Tx = F<F<a(a)>(F<a(a)>)>;
    Tx x;

    f2(Tx _x): x(_x) {}
    
    using Ty = F<a(a)>;
    F<a(a)> operator()(Ty y) {
        return f3<a>{x, y};
    }
};

template <class a>
struct f1 {
    using Tx = F<F<a(a)>(F<a(a)>)>;
    F<F<a(a)>(F<a(a)>)> operator()(Tx x) {
        return f2<a>{x};
    }
};

template <class a>
struct f5 {
    using Tx = F<a(a)>;
    Tx x;

    f5(Tx _x): x(_x) {}
    
    a operator()(a y) {
        return 1 + x(y);
    }
};

template <class a>
struct f4 {
    using Tx = F<a(a)>;
    F<a(a)> operator()()
}
*/

#include <iostream>

struct error {};

template <int v>
struct Int {
    constexpr static int value = v;

    static void show() {
        std::cout << v << '\n';
    }
};

template <class x, class y>
struct IntAdder {};
template <int x, int y>
struct IntAdder<Int<x>, Int<y>> {
    using result = Int<x + y>;
};

template <class L, class R>
using IntMultiply = Int<L::value * R::value>;

/*
struct succ {
    template <class x>
    using apply = IntAdd<x, Int<1>>;
};

template <class f>
struct f1 {
    template <class x>
    using apply = typename f::apply<typename f::apply<x>>;
};

struct twice {
    template <class f>
    using apply = f1<f>;
};

using five = twice::apply<succ>::apply<Int<3>>;
*/

// (\x: (a->a)->(a->a). \y: a->a. \z: a. x y z) (\x: a->a. \y: a. + 1 (x y)) (\x: int. * 3 x) 234

template <class x, class y>
struct f3 {
    template <class z>
    using apply = typename x::apply<y>::apply<z>;
};

template <class x>
struct f2 {
    template <class y>
    using apply = f3<x, y>;
};

struct f1 {
    template <class x>
    using apply = f2<x>;
};

template <class x>
struct f5 {
    template <class y>
    using apply = typename IntAdder<Int<1>, typename x::apply<y>>::result;
};

struct f4 {
    template <class x>
    using apply = f5<x>;
};

struct f6 {
    template <class x>
    using apply = IntMultiply<Int<3>, x>;
};

using result = f1::apply<f4>::apply<f6>::apply<Int<234>>;

/*
data Bool = True | False
data BoolList = Empty | List Bool BoolList
*/

struct True {};
struct False {};
struct Empty {};

template <class p1, class p2>
struct List {
    using member1 = p1;
    using member2 = p2;
};
template <class _param0>
struct ListCurried1 {
    template <class _param1>
    using apply = List<_param0, _param1>;
};
struct ListCurried0 {
    template <class _param0>
    using apply = ListCurried1<_param0>;
};

/*
\x.
match x with
| Empty -> 0
| List head rest -> (
    match head with
    | True -> 1
    | False -> 0
) + 2
*/


template <class x, class head, class rest, class _param>
struct m2 {};

template <class x, class head, class rest>
struct m2<x, head, rest, True> {
    using result = Int<1>;
};

template <class x, class head, class rest>
struct m2<x, head, rest, False> {
    using result = Int<0>;
};

template <class x, class _param>
struct m1 {};

template <class x>
struct m1<x, Empty> {
    using result = Int<0>;
};

template <class x, class head, class rest>
struct m1<x, List<head, rest>> {
    using result = typename IntAdder<typename m2<x, head, rest, head>::result, Int<2>>::result;
};

struct f7 {
    template <class x>
    using apply = typename m1<x, x>::result;
};

int main() {
    f7::apply<Empty>::show();
    f7::apply<ListCurried0::apply<True>::apply<Empty>>::show();
    f7::apply<ListCurried0::apply<False>::apply<Empty>>::show();
}