import sys
import numpy as np


def main():
    solve(np.fromstring(open(0).read(), dtype=np.int64, sep=' '))


if __name__ == "__main__":
    if sys.argv[-1] == 'ONLINE_JUDGE':
        import typing
        import numba
        try:
            from numba.experimental import jitclass
        except ImportError:
            from numba import jitclass
        from numba.pycc import CC

        @numba.njit('int64(int64)')
        def _ceil_pow2(n: int) -> int:
            x = 0
            while (1 << x) < n:
                x += 1

            return x

        TYPE_S = numba.types.int64
        TYPE_F = numba.types.int64

        @numba.njit('int64(int64, int64)')
        def f(a, b):
            return a if a > b else b

        TYPE_FUNC = numba.typeof(f)

        @jitclass([("_op", TYPE_FUNC),
                   ("_e", TYPE_S),
                   ("_mapping", TYPE_FUNC),
                   ("_composition", TYPE_FUNC),
                   ("_id", TYPE_F),
                   ("_n", numba.types.int64),
                   ("_log", numba.types.int64),
                   ("_size", numba.types.int64),
                   ("_d", TYPE_S[:]),
                   ("_lz", TYPE_F[:]),
                   ])
        # ref:
        # https://github.com/not522/ac-library-python/blob/a30b7e590271d7b77459946695ae8ce984e50f0a/atcoder/lazysegtree.py
        class LazySegTree:
            def __init__(
                    self,
                    op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                    e: typing.Any,
                    mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
                    composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
                    id_: typing.Any,
                    v: typing.Union[int, typing.List[typing.Any]]) -> None:
                self._op = op
                self._e = e
                self._mapping = mapping
                self._composition = composition
                self._id = id_

                # if isinstance(v, int):
                #     v = [e] * v

                self._n, = v.shape
                self._log = _ceil_pow2(self._n)
                self._size = 1 << self._log
                self._d = np.full(2 * self._size, e)
                self._lz = np.full(self._size, self._id)
                self._d[self._size: self._size + self._n] = v
                # for i in range(self._n):
                #     self._d[self._size + i] = v[i]
                for i in range(self._size - 1, 0, -1):
                    self._update(i)

            def set(self, p: int, x: typing.Any) -> None:
                assert 0 <= p < self._n

                p += self._size
                for i in range(self._log, 0, -1):
                    self._push(p >> i)
                self._d[p] = x
                for i in range(1, self._log + 1):
                    self._update(p >> i)

            def get(self, p: int) -> typing.Any:
                assert 0 <= p < self._n

                p += self._size
                for i in range(self._log, 0, -1):
                    self._push(p >> i)
                return self._d[p]

            def prod(self, left: int, right: int) -> typing.Any:
                assert 0 <= left <= right <= self._n

                if left == right:
                    return self._e

                left += self._size
                right += self._size

                for i in range(self._log, 0, -1):
                    if ((left >> i) << i) != left:
                        self._push(left >> i)
                    if ((right >> i) << i) != right:
                        self._push(right >> i)

                sml = self._e
                smr = self._e
                while left < right:
                    if left & 1:
                        sml = self._op(sml, self._d[left])
                        left += 1
                    if right & 1:
                        right -= 1
                        smr = self._op(self._d[right], smr)
                    left >>= 1
                    right >>= 1

                return self._op(sml, smr)

            def all_prod(self) -> typing.Any:
                return self._d[1]

            def apply(self, left: int, right: typing.Optional[int] = None,
                      f: typing.Optional[typing.Any] = None) -> None:
                assert f is not None

                if right is None:
                    p = left
                    assert 0 <= left < self._n

                    p += self._size
                    for i in range(self._log, 0, -1):
                        self._push(p >> i)
                    self._d[p] = self._mapping(f, self._d[p])
                    for i in range(1, self._log + 1):
                        self._update(p >> i)
                else:
                    assert 0 <= left <= right <= self._n
                    if left == right:
                        return

                    left += self._size
                    right += self._size

                    for i in range(self._log, 0, -1):
                        if ((left >> i) << i) != left:
                            self._push(left >> i)
                        if ((right >> i) << i) != right:
                            self._push((right - 1) >> i)

                    l2 = left
                    r2 = right
                    while left < right:
                        if left & 1:
                            self._all_apply(left, f)
                            left += 1
                        if right & 1:
                            right -= 1
                            self._all_apply(right, f)
                        left >>= 1
                        right >>= 1
                    left = l2
                    right = r2

                    for i in range(1, self._log + 1):
                        if ((left >> i) << i) != left:
                            self._update(left >> i)
                        if ((right >> i) << i) != right:
                            self._update((right - 1) >> i)

            def max_right(self, left: int,
                          g: typing.Callable[[typing.Any], bool]) -> int:
                assert 0 <= left <= self._n
                assert g(self._e)

                if left == self._n:
                    return self._n

                left += self._size
                for i in range(self._log, 0, -1):
                    self._push(left >> i)

                sm = self._e
                first = True
                while first or (left & -left) != left:
                    first = False
                    while left % 2 == 0:
                        left >>= 1
                    if not g(self._op(sm, self._d[left])):
                        while left < self._size:
                            self._push(left)
                            left *= 2
                            if g(self._op(sm, self._d[left])):
                                sm = self._op(sm, self._d[left])
                                left += 1
                        return left - self._size
                    sm = self._op(sm, self._d[left])
                    left += 1

                return self._n

            def min_left(self, right: int, g: typing.Any) -> int:
                assert 0 <= right <= self._n
                assert g(self._e)

                if right == 0:
                    return 0

                right += self._size
                for i in range(self._log, 0, -1):
                    self._push((right - 1) >> i)

                sm = self._e
                first = True
                while first or (right & -right) != right:
                    first = False
                    right -= 1
                    while right > 1 and right % 2:
                        right >>= 1
                    if not g(self._op(self._d[right], sm)):
                        while right < self._size:
                            self._push(right)
                            right = 2 * right + 1
                            if g(self._op(self._d[right], sm)):
                                sm = self._op(self._d[right], sm)
                                right -= 1
                        return right + 1 - self._size
                    sm = self._op(self._d[right], sm)

                return 0

            def _update(self, k: int) -> None:
                self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

            def _all_apply(self, k: int, f: typing.Any) -> None:
                self._d[k] = self._mapping(f, self._d[k])
                if k < self._size:
                    self._lz[k] = self._composition(f, self._lz[k])

            def _push(self, k: int) -> None:
                self._all_apply(2 * k, self._lz[k])
                self._all_apply(2 * k + 1, self._lz[k])
                self._lz[k] = self._id

        @numba.njit('void(int64[:])', cache=True)
        def solve(inp):
            w, n = inp[:2]
            sg = LazySegTree(f, 0, f, f, 0, np.zeros(w))
            for i in range(n):
                l = inp[i * 2 + 2]
                r = inp[i * 2 + 3]
                l -= 1
                x = sg.prod(l, r) + 1
                print(x)
                sg.apply(l, r, x)

        cc = CC('my_module')
        cc.export('solve', 'void(int64[:])')(solve)
        cc.compile()
    else:
        from my_module import solve
        main()
