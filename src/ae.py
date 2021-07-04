import sys

input = sys.stdin.readline


def fill_grundy():
    grundy = [[0 for j in range(1500)] for i in range(51)]
    for i in range(51):
        for j in range(1440):
            exist = [False for _ in range(800)]
            if i > 0:
                exist[grundy[i - 1][j + i]] = True
            for k in range(1, j // 2 + 1):
                exist[grundy[i][j - k]] = True
            g = 0
            while True:
                if not exist[g]:
                    break
                g += 1
            grundy[i][j] = g

    return grundy[:][: 51]


def main():
    grundy = fill_grundy()
    _ = int(input())
    w = list(map(int, input().split()))
    b = list(map(int, input().split()))
    g = 0
    for i, j in zip(w, b):
        g ^= grundy[i][j]
    print('First' if g > 0 else 'Second')


if __name__ == "__main__":
    main()
