import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow

input = sys.stdin.readline


def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    S = n
    T = n + 1
    frm = []
    to = []
    cap = []
    inf = 1 << 30
    for i in range(n):
        frm.append(S)
        to.append(i)
        cap.append(w)
        frm.append(i)
        to.append(T)
        cap.append(a[i])

    for i in range(n):
        v = [int(j) - 1 for j in input().split()[1:]]
        for j in v:
            frm.append(i)
            to.append(j)
            cap.append(inf)

    mat = csr_matrix((cap, (frm, to)), (n + 2, n + 2))
    print(sum(a) - maximum_flow(mat, S, T).flow_value)


if __name__ == "__main__":
    main()
