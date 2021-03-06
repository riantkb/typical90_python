import sys
import numpy as np
import numba
try:
    from numba.experimental import jitclass
except ImportError:
    from numba import jitclass

input = sys.stdin.readline


@jitclass([("n", numba.int32), ("data", numba.int64[:]), ])
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = np.zeros(n, dtype=np.int64)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.data[i - 1] += x
            i += i & -i

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def sum(self, l, r):
        return self._sum(r) - self._sum(l)


@numba.njit('int64(int32, int64[:, :])', cache=True)
def solve(n, p):
    bit = BIT(n)
    ans = 0
    for i in range(len(p)):
        l, r = p[i]
        ans += bit.sum(l + 1, r)
        bit.add(r, 1)

    return ans


def main():
    n, m = map(int, input().split())
    p = [[int(x) - 1 for x in input().split()] for _ in range(m)]
    p.sort(key=lambda x: (x[0], -x[1]))
    print(solve(n, np.array(p, dtype=np.int64)))


if __name__ == "__main__":
    main()
