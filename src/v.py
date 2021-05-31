import sys
from math import gcd

input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())
    g = gcd(gcd(a, b), c)
    print((a + b + c) // g - 3)


if __name__ == "__main__":
    main()
