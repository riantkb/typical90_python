import sys
import math

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    print(a // g * b if a // g <= 10 ** 18 // b else "Large")


if __name__ == "__main__":
    main()
