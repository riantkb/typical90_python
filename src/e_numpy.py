import numpy as np


def mul(A, B, b, p):
    mod = 1000000007
    res = np.zeros(b, dtype=np.int64)
    BB = np.concatenate((B, B))
    for i in range(b):
        s = -i * p % b
        res += A[i] * BB[s:s + b] % mod

    return res % mod


def main():
    n, b, _ = map(int, input().split())
    c = np.array(list(map(int, input().split())))
    res = np.zeros(b, dtype=np.int64)
    res[0] = 1
    p = 10
    a = np.zeros(b, dtype=np.int64)
    for i in c:
        a[i % b] += 1

    while n > 0:
        if n % 2 == 1:
            res = mul(res, a, b, p)
        a = mul(a, a, b, p)
        p = p * p % b
        n //= 2

    print(res[0])


if __name__ == "__main__":
    main()
