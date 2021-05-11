import sys

input = sys.stdin.readline


def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extgcd(b, a % b)
    y -= a // b * x
    return g, x, y


def main():
    n = int(input())
    a, b, c = reversed(sorted(map(int, input().split())))
    lim = 10000
    ans = lim
    g, x, y = extgcd(b, c)
    for i in range(lim):
        rem = n - a * i
        if rem >= 0 and rem % g == 0:
            j = x * (rem // g)
            k = y * (rem // g)
            tk = k % (b // g)
            j -= (tk - k) // (b // g) * (c // g)
            k = tk
            if j >= 0:
                ans = min(ans, i + j + k)

    print(ans)


if __name__ == "__main__":
    main()
