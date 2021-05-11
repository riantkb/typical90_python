import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a, b, c = map(int, input().split())
    lim = 10000
    ans = lim
    for i in range(lim):
        for j in range(lim):
            rem = n - a * i - b * j
            if rem < 0:
                break
            if rem % c == 0:
                ans = min(ans, i + j + rem // c)

    print(ans)


if __name__ == "__main__":
    main()
