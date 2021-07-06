import sys
from collections import deque

input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    si, sj = (int(i) - 1 for i in input().split())
    gi, gj = (int(i) - 1 for i in input().split())
    valid = [[i != '#' for i in input()] for _ in range(h)]
    idx0 = [[-1 for j in i] for i in valid]
    idx1 = [[-1 for j in i] for i in valid]
    edge = []
    for i in range(h):
        for j in range(w):
            if not valid[i][j]:
                continue
            if i > 0 and valid[i - 1][j]:
                idx0[i][j] = idx0[i - 1][j]
            else:
                idx0[i][j] = len(edge)
                edge.append([])
            if j > 0 and valid[i][j - 1]:
                idx1[i][j] = idx1[i][j - 1]
            else:
                idx1[i][j] = len(edge)
                edge.append([])

            edge[idx0[i][j]].append(idx1[i][j])
            edge[idx1[i][j]].append(idx0[i][j])

    dist = [-1 for _ in edge]
    q = deque()
    dist[idx0[si][sj]] = 0
    dist[idx1[si][sj]] = 0
    q.append(idx0[si][sj])
    q.append(idx1[si][sj])
    while q:
        p = q.popleft()
        for e in edge[p]:
            if dist[e] == -1:
                dist[e] = dist[p] + 1
                q.append(e)

    print(min(dist[idx0[gi][gj]], dist[idx1[gi][gj]]))


if __name__ == "__main__":
    main()
