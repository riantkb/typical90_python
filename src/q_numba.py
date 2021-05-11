import sys
import numpy as np
from numba import njit

input = sys.stdin.readline


@njit('void(int64[:], int32, int64)', cache=True)
def bit_add(data, i, x):
    i += 1
    while i <= len(data):
        data[i - 1] += x
        i += i & -i


@njit('int64(int64[:], int32)', cache=True)
def _bit_sum(data, r):
    s = 0
    while r > 0:
        s += data[r - 1]
        r -= r & -r
    return s


@njit('int64(int64[:], int32, int32)', cache=True)
def bit_sum(data, l, r):
    return _bit_sum(data, r) - _bit_sum(data, l)


@njit('int64(int32, int64[:, :])', cache=True)
def solve(n, p):
    bit = np.zeros(n, dtype=np.int64)
    ans = 0
    for i in range(len(p)):
        l, r = p[i]
        ans += bit_sum(bit, l + 1, r)
        bit_add(bit, r, 1)

    return ans


def main():
    n, m = map(int, input().split())
    p = [[int(x) - 1 for x in input().split()] for _ in range(m)]
    p.sort(key=lambda x: (x[0], -x[1]))
    print(solve(n, np.array(p, dtype=np.int64)))


if __name__ == "__main__":
    main()
