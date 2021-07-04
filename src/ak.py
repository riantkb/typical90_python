import sys

input = sys.stdin.readline


def main():
    w, n = map(int, input().split())
    p = [tuple(map(int, input().split())) for _ in range(n)]
    p.sort(key=lambda x: x[1] - x[0])
    inf = 1 << 60
    dp = [-inf for _ in range(w + 1)]
    dp[0] = 0
    ans = -inf
    for l, r, v in p:
        ans = max(ans, max(dp[w - r: w - l + 1]) + v)
        for i in range(w, l - 1, -1):
            dp[i] = max(dp[i], dp[i - l] + v)
            if i >= r:
                dp[i] = max(dp[i], dp[i - r] + v)

    print(ans if ans > 0 else -1)


if __name__ == "__main__":
    main()
