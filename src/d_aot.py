import sys
import numpy as np


def main():
    inp = np.fromstring(open(0).read(), dtype=np.int32, sep=' ')
    h, w = inp[:2]
    a = inp[2:].reshape(h, w)
    solve(a)


if __name__ == "__main__":
    if sys.argv[-1] == 'ONLINE_JUDGE':
        from numba.pycc import CC

        def solve(a):
            h, w = a.shape
            rows = a.sum(axis=1).reshape(h, 1)
            cols = a.sum(axis=0).reshape(1, w)
            for i in np.ravel(-a + rows + cols):
                print(i)

        cc = CC('my_module')
        cc.export('solve', 'void(int32[:, :])')(solve)
        cc.compile()
    else:
        from my_module import solve
        main()
