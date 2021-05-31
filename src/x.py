import sys

input = sys.stdin.readline


def main():
    _, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dist = sum(abs(i - j) for i, j in zip(a, b))
    print('Yes' if dist <= k and dist % 2 == k % 2 else 'No')


if __name__ == "__main__":
    main()
