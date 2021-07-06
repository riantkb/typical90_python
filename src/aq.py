import sys
from collections import deque

input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    si, sj = (int(i) - 1 for i in input().split())
    gi, gj = (int(i) - 1 for i in input().split())
    valid = [[i != '#' for i in input()] for _ in range(h)]
    dist0 = [[1 << 30 for j in i] for i in valid]
    dist1 = [[1 << 30 for j in i] for i in valid]

    deq = deque()
    dist0[si][sj] = 0
    dist1[si][sj] = 0
    deq.append((si, sj, 0))
    deq.append((si, sj, 1))
    while deq:
        i, j, k = deq.popleft()
        if k == 0:
            d = dist0[i][j]
            for ni in range(i + 1, h):
                if not valid[ni][j] or dist0[ni][j] <= d:
                    break
                dist0[ni][j] = d
                if dist1[ni][j] > d + 1:
                    dist1[ni][j] = d + 1
                    deq.append((ni, j, 1))
            for ni in range(i - 1, -1, -1):
                if not valid[ni][j] or dist0[ni][j] <= d:
                    break
                dist0[ni][j] = d
                if dist1[ni][j] > d + 1:
                    dist1[ni][j] = d + 1
                    deq.append((ni, j, 1))
        else:
            d = dist1[i][j]
            for nj in range(j + 1, w):
                if not valid[i][nj] or dist1[i][nj] <= d:
                    break
                dist1[i][nj] = d
                if dist0[i][nj] > d + 1:
                    dist0[i][nj] = d + 1
                    deq.append((i, nj, 0))
            for nj in range(j - 1, -1, -1):
                if not valid[i][nj] or dist1[i][nj] <= d:
                    break
                dist1[i][nj] = d
                if dist0[i][nj] > d + 1:
                    dist0[i][nj] = d + 1
                    deq.append((i, nj, 0))

    print(min(dist0[gi][gj], dist1[gi][gj]))


if __name__ == "__main__":
    main()
