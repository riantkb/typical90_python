def main():
    mod = 1000000007
    _ = int(input())
    s = input()
    t = "atcoder"
    idx = {t[i]: i for i in range(len(t))}
    dp = [1 if i == 0 else 0 for i in range(len(t) + 1)]
    for c in s:
        if c in idx:
            dp[idx[c] + 1] = (dp[idx[c] + 1] + dp[idx[c]]) % mod

    print(dp[-1])


if __name__ == "__main__":
    main()
