import sys
import numpy as np
import numba
# from numba.experimental import jitclass
from numba import jitclass

input = sys.stdin.readline


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


def main():
    h, w = map(int, input().split())
    uf = union_find(h * w)
    painted = [False for _ in range(h * w)]
    adj = ((0, 1), (1, 0), (0, -1), (-1, 0))
    q = int(input())
    for _ in range(q):
        t, *a = [int(i) - 1 for i in input().split()]
        if t == 0:
            i, j = a
            painted[i * w + j] = True
            for di, dj in adj:
                ti = i + di
                tj = j + dj
                if 0 <= ti < h and 0 <= tj < w and painted[ti * w + tj]:
                    uf.union(i * w + j, ti * w + tj)
        else:
            i1, j1, i2, j2 = a
            print("Yes" if painted[i1 * w + j1]
                  and uf.same(i1 * w + j1, i2 * w + j2) else "No")


if __name__ == "__main__":
    main()
