import sys
from functools import lru_cache

sys.setrecursionlimit(2 ** 20)

input = sys.stdin.readline


def main():
    n = int(input()) * 2
    a = list(map(int, input().split()))
    delta = [[abs(i - j) for j in a] for i in a]

    @lru_cache(maxsize=None)
    def solve(l, r):
        if r - l == 0:
            return 0
        return min(solve(l + 1, j) + solve(j + 1, r)
                   + delta[l][j] for j in range(l + 1, r, 2))

    print(solve(0, n))


if __name__ == "__main__":
    main()
