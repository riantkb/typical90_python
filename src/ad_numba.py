import sys
import numpy as np
from numba import njit

input = sys.stdin.readline


@njit('int32(int32, int32)', cache=True)
def solve(n, k):
    cnt = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if cnt[i] == 0:
            cnt[i: n + 1: i] += 1

    return (cnt >= k).sum()


def main():
    n, k = map(int, input().split())
    print(solve(n, k))


if __name__ == "__main__":
    main()
