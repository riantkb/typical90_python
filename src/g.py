from bisect import bisect


def main():
    _ = int(input())
    a = sorted(map(int, input().split()))
    a = [-10**9] + a + [2 * 10**9]
    q = int(input())
    b = [int(input()) for _ in range(q)]
    for x in b:
        i = bisect(a, x)
        print(min(a[i] - x, x - a[i - 1]))


if __name__ == "__main__":
    main()
