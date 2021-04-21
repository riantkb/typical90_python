def mul(A, B, b, p):
    mod = 1000000007
    res = [0 for _ in range(b)]
    BB = B + B
    for i in range(b):
        s = -i * p % b
        for j in range(b):
            res[j] += A[i] * BB[s + j] % mod

    return [i % mod for i in res]


def main():
    n, b, _ = map(int, input().split())
    c = list(map(int, input().split()))
    res = [0 for _ in range(b)]
    res[0] = 1
    p = 10
    a = [0 for _ in range(b)]
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
