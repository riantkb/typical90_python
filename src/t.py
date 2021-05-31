import sys

input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())
    print("Yes" if a < c ** b else "No")


if __name__ == "__main__":
    main()
