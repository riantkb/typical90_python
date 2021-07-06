import sys
import numpy as np


def main():
    h, w = map(int, input().split())
    s = np.array([[c == '.' for c in input()]
                  for _ in range(h)], dtype=np.bool8)
    print(solve(s))


if __name__ == "__main__":
    if sys.argv[-1] == 'ONLINE_JUDGE':
        from numba.pycc import CC

        def solve(s):
            h, w = s.shape
            mod = 10 ** 9 + 7
            mask = (1 << (w + 1)) - 1

            def collision(j, b):
                return (j > 0 and b & 1
                        or j + 1 < w and (b >> (w - 2)) & 1
                        or (b >> (w - 1)) & 1
                        or j > 0 and (b >> w) & 1)

            states = []
            for i in range(w):
                lis = [0]
                for j in range(w + 1):
                    nex = []
                    t = (i + j - 1) % w
                    for k in lis:
                        nex.append(k << 1)
                        if not collision(t, k):
                            nex.append(k << 1 | 1)
                    lis = nex
                states.append(lis)

            indices = []
            for st in states:
                dic = {}
                for i, b in enumerate(st):
                    dic[b] = i
                indices.append(dic)
            # indices = [{b: i for i, b in enumerate(st)} for st in states]
            nexts = [[[indices[i - w + 1][st << 1 & mask],
                       indices[i - w + 1][(st << 1 | 1) & mask]
                       if not collision(i, st) else -1]
                      for st in states[i]] for i in range(w)]

            dp = [0 for _ in states[0]]
            dp[0] = 1

            for i in range(h):
                for j in range(w):
                    nex = [0 for _ in states[j - w + 1]]
                    for k, c in enumerate(dp):
                        for l in range(2):
                            nk = nexts[j][k][l]
                            if l == 0 or s[i][j] and nk != -1:
                                nex[nk] += c
                                if nex[nk] >= mod:
                                    nex[nk] -= mod

                    dp = nex

            res = 0
            for i in dp:
                res += i
            return res % mod

        cc = CC('my_module')
        cc.export('solve', 'int64(boolean[:, :])')(solve)
        cc.compile()

    else:
        from my_module import solve
        main()
