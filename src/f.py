def main():
    n, k = map(int, input().split())
    s = input()
    lis = []
    for i in range(n):
        while lis and len(lis) + n - i > k and lis[-1] > s[i]:
            lis.pop()
        if len(lis) < k:
            lis.append(s[i])

    print(*lis, sep='')


if __name__ == "__main__":
    main()
