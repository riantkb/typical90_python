import sys
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import dijkstra

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    a = [-1 for _ in range(m)]
    b = [-1 for _ in range(m)]
    c = [-1 for _ in range(m)]
    for i in range(m):
        a[i], b[i], c[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    mat = coo_matrix((c, (a, b)), (n, n))
    print(*dijkstra(mat, directed=False, indices=[0, n - 1])
          .astype('int32').sum(axis=0), sep='\n')


if __name__ == "__main__":
    main()
