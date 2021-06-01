import sys

input = sys.stdin.readline


def main():
    n = int(input())
    m = 1010
    imos = [[0 for j in range(m)] for i in range(m)]
    for _ in range(n):
        lx, ly, rx, ry = map(int, input().split())
        imos[lx][ly] += 1
        imos[lx][ry] -= 1
        imos[rx][ly] -= 1
        imos[rx][ry] += 1

    for i in range(m):
        for j in range(m - 1):
            imos[i][j + 1] += imos[i][j]
    for i in range(m - 1):
        for j in range(m):
            imos[i + 1][j] += imos[i][j]

    ans = [0 for _ in range(n + 1)]
    for i in imos:
        for j in i:
            ans[j] += 1

    print(*ans[1:], sep='\n')


if __name__ == "__main__":
    main()
