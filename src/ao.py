import sys
from math import gcd

input = sys.stdin.readline


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def convex_hull(ps):
    ps.sort()
    res = []
    for p in ps:
        while len(res) > 1 and cross((res[-1][0] - res[-2][0], res[-1][1] - res[-2][1]),
                                     (p[0] - res[-1][0], p[1] - res[-1][1])) <= 0:
            res.pop()
        res.append(p)
    t = len(res)
    for p in ps[-2::-1]:
        while len(res) > t and cross((res[-1][0] - res[-2][0], res[-1][1] - res[-2][1]),
                                     (p[0] - res[-1][0], p[1] - res[-1][1])) <= 0:
            res.pop()
        res.append(p)
    res.pop()
    return res


def area2(ps):
    n = len(ps)
    return sum(cross(ps[i], ps[i + 1 - n]) for i in range(n))


def main():
    n = int(input())
    ps = [tuple(map(int, input().split())) for _ in range(n)]
    ch = convex_hull(ps)
    m = len(ch)
    bound_cnt = 0
    for i in range(m):
        p, q = ch[i], ch[i + 1 - m]
        dx = abs(q[0] - p[0])
        dy = abs(q[1] - p[1])
        bound_cnt += gcd(dx, dy)
    inner_cnt = (area2(ch) - bound_cnt + 2) // 2
    print(bound_cnt + inner_cnt - n)


if __name__ == "__main__":
    main()
