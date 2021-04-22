import numpy as np
from numba import njit


@njit('void(int64[:], int64[:])', cache=True)
def solve(a, b):
    a.sort()
    idx = np.searchsorted(a, b)
    for x, i in zip(b, idx):
        print(min(a[i] - x, x - a[i - 1]))


def main():
    _ = int(input())
    a = np.array(list(map(int, input().split())) + [-10**9, 2 * 10**9])
    q = int(input())
    b = np.array([int(input()) for _ in range(q)])
    solve(a, b)


if __name__ == "__main__":
    main()
