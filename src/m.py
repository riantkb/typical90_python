import sys
import heapq

input = sys.stdin.readline


def dijkstra(edge, s):
    inf = 2**60
    dist = [0 if i == s else inf for i in range(len(edge))]
    q = [(0, s)]
    while q:
        d, p = heapq.heappop(q)
        if dist[p] < d:
            continue
        for c, to in edge[p]:
            if dist[to] > d + c:
                dist[to] = d + c
                heapq.heappush(q, (dist[to], to))

    return dist


def main():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append((c, v))
        edge[v].append((c, u))
    d0 = dijkstra(edge, 0)
    d1 = dijkstra(edge, n - 1)
    print(*(sum(i) for i in zip(d0, d1)), sep='\n')


if __name__ == "__main__":
    main()
