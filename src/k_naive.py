def main():
    n = int(input())
    works = [tuple(map(int, input().split())) for _ in range(n)]
    works.sort(key=lambda x: x[0])

    dp = [0 for _ in range(5010)]
    for d, c, s in works:
        for i in range(d, c - 1, -1):
            dp[i] = max(dp[i], dp[i - c] + s)

    print(max(dp))


if __name__ == "__main__":
    main()
