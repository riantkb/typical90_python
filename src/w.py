def main():
    mod = 10 ** 9 + 7
    h, w = map(int, input().split())
    s = [[c == '.' for c in input()] for _ in range(h)]

    mask = (1 << (w + 1)) - 1

    def collision(j, b):
        return (j > 0 and b & 1
                or j + 1 < w and (b >> (w - 2)) & 1
                or (b >> (w - 1)) & 1
                or j > 0 and (b >> w) & 1)

    states = [None for _ in range(w)]
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
        states[i] = lis

    indices = [{b: i for i, b in enumerate(st)} for st in states]
    nexts = [[[indices[i + 1 - w][st << 1 & mask],
               indices[i + 1 - w][(st << 1 | 1) & mask]
               if not collision(i, st) else -1]
              for st in states[i]] for i in range(w)]

    dp = [0 for _ in states[0]]
    dp[0] = 1

    for i in range(h):
        for j in range(w):
            nex = [0 for _ in states[j + 1 - w]]
            for k, c in enumerate(dp):
                nk = nexts[j][k][0]
                nex[nk] += c
                if nex[nk] >= mod:
                    nex[nk] -= mod
                if s[i][j] and nexts[j][k][1] != -1:
                    nk = nexts[j][k][1]
                    nex[nk] += c
                    if nex[nk] >= mod:
                        nex[nk] -= mod

            dp = nex

    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
