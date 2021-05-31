import sys

input = sys.stdin.readline


def main():
    n = int(input()) * 2
    a = list(map(int, input().split()))
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
    delta = [[abs(i - j) for j in a] for i in a]
    for k in range(2, n + 1, 2):
        for i in range(n + 1 - k):
            dp[i][i + k] = min(dp[i + 1][j] + dp[j + 1][i + k] + delta[i][j]
                               for j in range(i + 1, i + k, 2))

    print(dp[0][n])


if __name__ == "__main__":
    main()
