def main():
    _ = int(input())
    a = sorted(map(int, input().split()))
    a = [-10**9] + a + [2 * 10**9]
    q = int(input())
    b = [int(input()) for _ in range(q)]
    idx = sorted(range(q), key=lambda i: b[i])
    ans = [-1 for _ in range(q)]
    j = 0
    for i in idx:
        while a[j] < b[i]:
            j += 1

        ans[i] = min(b[i] - a[j - 1], a[j] - b[i])

    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
