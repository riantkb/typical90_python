import sys
from itertools import accumulate

input = sys.stdin.readline


def main():
    n = int(input())
    scores = [[0 for j in range(n)] for i in range(2)]
    for i in range(n):
        c, p = map(int, input().split())
        c -= 1
        scores[c][i] = p

    accums = [list(accumulate(s, initial=0)) for s in scores]
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        print(*(a[r] - a[l] for a in accums))


if __name__ == "__main__":
    main()
