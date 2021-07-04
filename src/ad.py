import sys

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    cnt = [0] * (n + 1)
    for i in range(2, n + 1):
        if cnt[i] == 0:
            for j in range(i, n + 1, i):
                cnt[j] += 1

    print(sum(c >= k for c in cnt))


if __name__ == "__main__":
    main()
