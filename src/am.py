import sys

sys.setrecursionlimit(2 ** 20)

input = sys.stdin.readline


def dfs(p, par, edge):
    res = 0
    cnt = 1
    for e in edge[p]:
        if e == par:
            continue
        r, c = dfs(e, p, edge)
        res += r
        cnt += c
    res += cnt * (len(edge) - cnt)
    return res, cnt


def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = (int(i) - 1 for i in input().split())
        edge[u].append(v)
        edge[v].append(u)
    print(dfs(0, -1, edge)[0])


if __name__ == "__main__":
    main()
