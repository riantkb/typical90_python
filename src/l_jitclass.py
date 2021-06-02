import numpy as np
import numba
try:
    from numba.experimental import jitclass
except ImportError:
    from numba import jitclass


@jitclass([("parent_or_size", numba.int32[:]), ])
class union_find:
    def __init__(self, n):
        self.parent_or_size = np.full(n, -1, dtype=np.int32)

    def find(self, x):
        p = x
        while self.parent_or_size[p] >= 0:
            p = self.parent_or_size[p]
        while self.parent_or_size[x] >= 0:
            tmp = self.parent_or_size[x]
            self.parent_or_size[x] = p
            x = tmp
        return p

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parent_or_size[self.find(x)]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.size(x) < self.size(y):
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return True


@numba.njit('void(int32[:])', cache=True)
def main(inp):
    h, w, q = inp[:3]
    uf = union_find(h * w)
    painted = np.zeros((h, w), dtype=np.bool8)
    adj = ((0, 1), (1, 0), (0, -1), (-1, 0))
    idx = 3
    for _ in range(q):
        t = inp[idx]
        idx += 1
        if t == 1:
            i, j = inp[idx: idx + 2] - 1
            idx += 2
            painted[i, j] = True
            for di, dj in adj:
                ti = i + di
                tj = j + dj
                if 0 <= ti < h and 0 <= tj < w and painted[ti, tj]:
                    uf.union(i * w + j, ti * w + tj)
        else:
            i1, j1, i2, j2 = inp[idx: idx + 4] - 1
            idx += 4
            print("Yes" if painted[i1, j1]
                  and uf.same(i1 * w + j1, i2 * w + j2) else "No")


if __name__ == "__main__":
    main(np.fromstring(open(0).read(), dtype=np.int32, sep=' '))
