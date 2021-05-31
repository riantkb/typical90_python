import sys
import numpy as np

input = sys.stdin.readline


def solve(a):
    n = a.shape[0]
    dp = np.zeros((n + 1, n + 1), dtype=np.int32)
    delta = np.abs(a.reshape((1, n)) - a.reshape((n, 1)))

    for k in range(2, n + 1, 2):
        for i in range(n + 1 - k):
            dp[i][i + k] = np.min(dp[i + 1, i + 1: i + k: 2]
                                  + dp.T[i + k, i + 1 + 1: i + k + 1: 2]
                                  + delta[i, i + 1: i + k: 2])

    return dp[0, n]


def main():
    _ = int(input())
    a = np.array(list(map(int, input().split())), dtype=np.int32)
    print(solve(a))


if __name__ == "__main__":
    main()
