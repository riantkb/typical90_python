import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    a = [-1 for _ in range(m)]
    b = [-1 for _ in range(m)]
    for i in range(m):
        a[i], b[i] = (int(j) - 1 for j in input().split())

    mat = csr_matrix(([1 for _ in range(m)], (a, b)), (n, n))
    _, labels = connected_components(mat, connection='strong')
    cnt = [0 for _ in range(n)]
    for i in labels:
        cnt[i] += 1
    print(sum(i * (i - 1) // 2 for i in cnt))


if __name__ == "__main__":
    main()
