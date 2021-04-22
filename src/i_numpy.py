import numpy as np
from numba import njit


@njit('float64(complex128[:])', cache=True)
def solve(points):
    n = points.shape[0]
    ans = 0.0
    for i in range(n):
        atan = np.append(np.sort(np.angle(np.append(
            points[:i], points[i + 1:]) - points[i], deg=True)), 10000.0)
        idx = np.searchsorted(atan, atan[:-1] + 180)
        ans = max([max(atan[j - 1] - x, 360 + x - atan[j])
                   for j, x in zip(idx, atan[:-1])] + [ans])

    return ans


def main():
    n = int(input())
    points = np.array([complex(*map(int, input().split())) for _ in range(n)])
    print(solve(points))


if __name__ == "__main__":
    main()
