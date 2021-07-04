import sys
import numpy as np

sys.setrecursionlimit(2 ** 20)


def main():
    solve(np.fromstring(open(0).read(), dtype=np.int32, sep=' '))


if __name__ == "__main__":
    if sys.argv[-1] == 'ONLINE_JUDGE':
        import numba
        try:
            from numba.experimental import jitclass
        except ImportError:
            from numba import jitclass
        from numba.pycc import CC

        @jitclass([('__m', numba.types.int32),
                   ('__parent', numba.types.int32[:, :]),
                   ('__depth', numba.types.int32[:]),
                   ])
        class LCATree:
            def __init__(self, n, edges, e_idx, root):
                self.__m = 1
                while (1 << self.__m) < n:
                    self.__m += 1
                self.__parent = np.full((n, self.__m), -1, dtype=np.int32)
                self.__depth = np.full(n, -1, dtype=np.int32)
                self.__depth[root] = 0
                q = []
                q.append(root)
                while q:
                    p = q.pop()
                    for e in edges[e_idx[p]: e_idx[p + 1]]:
                        if self.__depth[e] != -1:
                            continue
                        self.__depth[e] = self.__depth[p] + 1
                        self.__parent[e, 0] = p
                        for i in range(1, self.__m):
                            self.__parent[e,
                                          i] = self.__parent[self.__parent[e,
                                                                           i - 1],
                                                             i - 1]
                            if self.__parent[e, i] == -1:
                                break

                        q.append(e)

            def __climb(self, p, l):
                for i in range(self.__m):
                    if l >> i & 1:
                        p = self.__parent[p, i]

                return p

            def lca(self, p, q):
                if self.__depth[p] > self.__depth[q]:
                    p = self.__climb(p, self.__depth[p] - self.__depth[q])
                if self.__depth[p] < self.__depth[q]:
                    q = self.__climb(q, self.__depth[q] - self.__depth[p])
                if p == q:
                    return p

                for i in range(self.__m - 1, -1, -1):
                    if self.__parent[p, i] != self.__parent[q, i]:
                        p = self.__parent[p, i]
                        q = self.__parent[q, i]

                return self.__parent[p, 0]

            def dist(self, p, q):
                return (self.__depth[p] + self.__depth[q]
                        - self.__depth[self.lca(p, q)] * 2)

        @numba.njit('int32(int32, int32, int32, int32[:], int32[:], int32[:])')
        def dfs(p, par, cnt, res, edges, e_idx):
            res[p] = cnt
            cnt += 1
            for e in edges[e_idx[p]: e_idx[p + 1]]:
                if e != par:
                    cnt = dfs(e, p, cnt, res, edges, e_idx)

            return cnt

        @numba.njit('int32[:](int32, int32[:], int32[:], int32)')
        def get_preorder(n, edges, e_idx, root):
            res = np.full(n, -1, dtype=np.int32)
            dfs(root, -1, 0, res, edges, e_idx)
            return res

        def solve(inp):
            n = inp[0]
            deg = np.zeros(n, dtype=np.int32)
            for i in range(n - 1):
                u, v = inp[i * 2 + 1] - 1, inp[i * 2 + 2] - 1
                deg[u] += 1
                deg[v] += 1

            e_idx = np.zeros(n + 1, dtype=np.int32)
            for i in range(n):
                e_idx[i + 1] = e_idx[i] + deg[i]

            edges = np.full((n - 1) * 2, -1, dtype=np.int32)
            cnt = np.zeros(n, dtype=np.int32)
            for i in range(n - 1):
                u, v = inp[i * 2 + 1] - 1, inp[i * 2 + 2] - 1
                edges[e_idx[u] + cnt[u]] = v
                edges[e_idx[v] + cnt[v]] = u
                cnt[u] += 1
                cnt[v] += 1

            lca = LCATree(n, edges, e_idx, 0)
            preorder = get_preorder(n, edges, e_idx, 0)
            q = inp[n * 2 - 1]
            head = n * 2
            for _ in range(q):
                k = inp[head]
                head += 1
                a = inp[head: head + k] - 1
                head += k
                key = np.array([preorder[i] for i in a], dtype=np.int32)
                order = np.argsort(key)
                ans = 0
                for i in range(k):
                    u, v = a[order[i]], a[order[i + 1 - k]]
                    ans += lca.dist(u, v)
                print(ans // 2)

        cc = CC('my_module')
        cc.export('solve', 'void(int32[:])')(solve)
        cc.compile()
    else:
        from my_module import solve
        main()
