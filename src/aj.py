import sys

input = sys.stdin.readline


def main():
    n, q = map(int, input().split())
    p = [None for _ in range(n)]
    for i in range(n):
        x, y = map(int, input().split())
        p[i] = (x + y, x - y, -x + y, -x - y)

    maxs = tuple(max(x[i] for x in p) for i in range(4))

    for _ in range(q):
        i = int(input()) - 1
        print(max(i - j for i, j in zip(maxs, p[i])))


if __name__ == "__main__":
    main()
