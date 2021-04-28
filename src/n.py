import sys

input = sys.stdin.readline


def main():
    _ = int(input())
    print(sum(abs(a - b)
              for a, b in zip(*(sorted(map(int, input().split())) for _ in range(2)))))


if __name__ == "__main__":
    main()
