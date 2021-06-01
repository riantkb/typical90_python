import sys
from collections import deque

input = sys.stdin.readline


def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = (int(i) - 1 for i in input().split())
        edge[u].append(v)
        edge[v].append(u)

    grp = [-1 for _ in edge]
    q = deque()
    grp[0] = 0
    q.append(0)
    while q:
        p = q.popleft()
        for e in edge[p]:
            if grp[e] == -1:
                grp[e] = 1 - grp[p]
                q.append(e)

    gi = sum(grp) * 2 >= n
    lis = [i + 1 for i, g in enumerate(grp) if g == gi]
    print(*lis[: n // 2])


if __name__ == "__main__":
    main()
