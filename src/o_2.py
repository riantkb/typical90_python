import sys
from itertools import accumulate

input = sys.stdin.readline

mod = 1000000007


def init_comb(n):
    global facts, invfacts
    facts = [i for i in range(n + 1)]
    facts[0] = 1
    facts = list(accumulate(facts, lambda x, y: x * y % mod))
    invfacts = [n + 1 - i for i in range(n + 1)]
    invfacts[0] = pow(facts[n], -1, mod)
    invfacts = list(reversed(list(accumulate(invfacts,
                                             lambda x, y: x * y % mod))))


def comb(n, r):
    if r < 0 or n < r:
        return 0
    return facts[n] * invfacts[r] * invfacts[n - r] % mod


def main():
    n = int(input())
    init_comb(n)
    for i in range(n):
        print(sum(comb(n - i * j, j + 1)
                  for j in range(n // (i + 1) + 2)) % mod)


if __name__ == "__main__":
    main()
