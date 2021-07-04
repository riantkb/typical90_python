import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    valid = [[True for j in range(n)] for i in range(n)]
    m = int(input())
    for _ in range(m):
        x, y = [int(i) - 1 for i in input().split()]
        valid[x][y] = False
        valid[y][x] = False

    inf = 1 << 30
    dp = [[inf for j in range(n)] for i in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = a[i][0]

    for i in range(1, 1 << n):
        bc = sum(i >> j & 1 for j in range(n))
        for j in range(n):
            for k in range(n):
                if valid[j][k] and (i >> k & 1) == 0:
                    dp[i | 1 << k][k] = min(dp[i | 1 << k][k],
                                            dp[i][j] + a[k][bc])

    ans = min(dp[-1])
    print(ans if ans < inf else -1)


if __name__ == "__main__":
    main()
