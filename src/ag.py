import sys

input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    if h == 1 or w == 1:
        print(h * w)
    else:
        print(((h + 1) // 2) * ((w + 1) // 2))


if __name__ == "__main__":
    main()
