import sys
from collections import deque

sys.setrecursionlimit(2 ** 20)

input = sys.stdin.readline


class LCATree:
    def __init__(self, edge, root=0):
        n = len(edge)
        self.__m = 1
        while (1 << self.__m) < n:
            self.__m += 1
        self.__parent = [[-1 for j in range(self.__m)] for i in range(n)]
        self.__depth = [-1 for _ in range(n)]
        self.__depth[root] = 0
        q = deque()
        q.append(root)
        while q:
            p = q.popleft()
            for e in edge[p]:
                if self.__depth[e] != -1:
                    continue
                self.__depth[e] = self.__depth[p] + 1
                self.__parent[e][0] = p
                for i in range(1, self.__m):
                    self.__parent[e][i] = self.__parent[self.__parent[e]
                                                        [i - 1]][i - 1]
                    if self.__parent[e][i] == -1:
                        break

                q.append(e)

    def __climb(self, p, l):
        for i in range(self.__m):
            if l >> i & 1:
                p = self.__parent[p][i]

        return p

    def lca(self, p, q):
        if self.__depth[p] > self.__depth[q]:
            p = self.__climb(p, self.__depth[p] - self.__depth[q])
        if self.__depth[p] < self.__depth[q]:
            q = self.__climb(q, self.__depth[q] - self.__depth[p])
        if p == q:
            return p

        for i in range(self.__m - 1, -1, -1):
            if self.__parent[p][i] != self.__parent[q][i]:
                p = self.__parent[p][i]
                q = self.__parent[q][i]

        return self.__parent[p][0]

    def dist(self, p, q):
        return (self.__depth[p] + self.__depth[q]
                - self.__depth[self.lca(p, q)] * 2)


def get_preorder(edge, root=0):

    def dfs(p, par, cnt, res):
        res[p] = cnt
        cnt += 1
        for e in edge[p]:
            if e != par:
                cnt = dfs(e, p, cnt, res)

        return cnt

    res = [-1 for _ in edge]
    dfs(root, -1, 0, res)
    return res


def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = (int(i) - 1 for i in input().split())
        edge[u].append(v)
        edge[v].append(u)

    lca = LCATree(edge)
    preorder = get_preorder(edge)
    q = int(input())
    for _ in range(q):
        v = [int(i) - 1 for i in input().split()][1:]
        v.sort(key=lambda x: preorder[x])
        print(sum(lca.dist(i, j) for i, j in zip(v, v[1:] + v[:1])) // 2)


if __name__ == "__main__":
    main()
