import sys

input = sys.stdin.readline


def main():
    k = int(input())
    if k % 9 != 0:
        print(0)
        return

    mod = 10 ** 9 + 7
    dp = [1]
    for _ in range(k):
        dp.append(sum(dp[-9:]) % mod)
    print(dp[-1])


if __name__ == "__main__":
    main()
