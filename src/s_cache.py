import sys

sys.setrecursionlimit(2 ** 20)

input = sys.stdin.readline


def main():
    n = int(input()) * 2
    a = list(map(int, input().split()))
    delta = [[abs(i - j) for j in a] for i in a]
    memo = [[-1 if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]

    def solve(l, r):
        if memo[l][r] != -1:
            return memo[l][r]
        memo[l][r] = min(solve(l + 1, j) + solve(j + 1, r)
                         + delta[l][j] for j in range(l + 1, r, 2))
        return memo[l][r]

    print(solve(0, n))


if __name__ == "__main__":
    main()
