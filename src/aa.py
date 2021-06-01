import sys

input = sys.stdin.readline


def main():
    n = int(input())
    se = set()
    for i in range(n):
        s = input().strip()
        if s not in se:
            print(i + 1)
            se.add(s)


if __name__ == "__main__":
    main()
