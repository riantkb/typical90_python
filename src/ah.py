import sys

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    cnt = 0
    j = 0
    ans = 0
    for i in range(n):
        while j < n and cnt <= k:
            if not a[j] in d:
                d[a[j]] = 0
            if d[a[j]] == 0:
                if cnt == k:
                    break
                cnt += 1
            d[a[j]] += 1
            j += 1
        ans = max(ans, j - i)
        d[a[i]] -= 1
        if d[a[i]] == 0:
            cnt -= 1

    print(ans)


if __name__ == "__main__":
    main()
