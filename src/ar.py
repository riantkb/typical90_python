import sys

input = sys.stdin.readline


def main():
    n, q = map(int, input().split())
    a = input().split()
    rot = 0
    for _ in range(q):
        t, x, y = (int(i) - 1 for i in input().split())
        if t == 0:
            a[x - rot], a[y - rot] = a[y - rot], a[x - rot]
        elif t == 1:
            rot = (rot + 1) % n
        else:
            print(a[x - rot])


if __name__ == "__main__":
    main()
