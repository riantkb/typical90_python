import sys
import math
from itertools import product

input = sys.stdin.readline


def main():
    n, b = map(int, input().split())
    lis = [[1] for _ in range(4)]
    for l, p in zip(lis, (2, 3, 5, 7)):
        while l[-1] * p <= n - b:
            l.append(l[-1] * p)

    def f(x):
        res = 1
        while x > 0:
            res *= x % 10
            x //= 10
        return res

    def check(x):
        return 1 <= x <= n and x - f(x) == b

    print((1 if check(b) else 0)
          + sum(check(math.prod(p) + b) for p in product(*lis)))


if __name__ == "__main__":
    main()
