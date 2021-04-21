from collections import deque


def get_diameter(edge):
    def get_farthest(edge, s):
        dist = [-1 for _ in edge]
        q = deque()
        dist[s] = 0
        q.append(s)
        while q:
            p = q.popleft()
            for e in edge[p]:
                if dist[e] == -1:
                    dist[e] = dist[p] + 1
                    q.append(e)

        far = max(range(len(edge)), key=lambda i: dist[i])
        return dist[far], far

    _, p = get_farthest(edge, 0)
    dist, q = get_farthest(edge, p)
    return dist, (p, q)


def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = (int(i) - 1 for i in input().split())
        edge[u].append(v)
        edge[v].append(u)

    print(get_diameter(edge)[0] + 1)


if __name__ == "__main__":
    main()
