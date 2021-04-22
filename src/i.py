import cmath
from bisect import bisect


def main():
    n = int(input())
    points = [complex(*map(int, input().split())) for _ in range(n)]
    ans = 0
    for p in points:
        atan = sorted(cmath.phase(o - p) for o in points if o != p)
        atan.append(100)
        for x in atan:
            i = bisect(atan, x + cmath.pi)
            ans = max(ans, atan[i - 1] - x, cmath.pi * 2 + x - atan[i])
            if i == len(atan) - 1:
                break

    print(ans / cmath.pi * 180)


if __name__ == "__main__":
    main()
