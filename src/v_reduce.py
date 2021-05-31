import sys
from math import gcd
from functools import reduce


input = sys.stdin.readline


def main():
    a = list(map(int, input().split()))
    g = reduce(gcd, a, 0)
    print(sum(a) // g - len(a))


if __name__ == "__main__":
    main()
