import sys

input = sys.stdin.readline


class BIT:
    def __init__(self, n):
        self.__n = n
        self.__data = [0] * n

    def add(self, i, x):
        i += 1
        while i <= self.__n:
            self.__data[i - 1] += x
            i += i & -i

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.__data[r - 1]
            r -= r & -r
        return s

    def sum(self, l, r):
        return self._sum(r) - self._sum(l)


def main():
    n, m = map(int, input().split())
    p = [tuple(int(x) - 1 for x in input().split()) for _ in range(m)]
    p.sort(key=lambda x: (x[0], -x[1]))
    bit = BIT(n)
    ans = 0
    for l, r in p:
        ans += bit.sum(l + 1, r)
        bit.add(r, 1)

    print(ans)


if __name__ == "__main__":
    main()
