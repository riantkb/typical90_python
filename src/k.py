import numpy as np


def main():
    n = int(input())
    works = [tuple(map(int, input().split())) for _ in range(n)]
    works.sort(key=lambda x: x[0])

    dp = np.zeros(5010, dtype=np.int64)
    for d, c, s in works:
        if c <= d:
            dp[c: d + 1] = np.maximum(dp[c: d + 1], dp[: d + 1 - c] + s)

    print(dp.max())


if __name__ == "__main__":
    main()
