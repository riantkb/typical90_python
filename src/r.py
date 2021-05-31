import sys
import math

input = sys.stdin.readline


def main():
    t = int(input())
    l, x, y = map(int, input().split())
    q = int(input())
    for _ in range(q):
        e = int(input())
        ty = -l / 2 * math.sin(e / t * math.pi * 2)
        tz = l / 2 * (1 - math.cos(e / t * math.pi * 2))
        print(math.degrees(math.atan2(tz, math.hypot(x, y - ty))))


if __name__ == "__main__":
    main()
