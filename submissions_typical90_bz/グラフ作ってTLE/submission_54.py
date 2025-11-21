def main():
    N, M = map(int, input().split())
    G = Graph(N, M)
    for i in range(M):
        a, b = map(int, input().split())
        G.append_edge(a, b)

    cnt = 0
    for i in range(N):
        tmp = 0
        for data in G.edge[i]:
            if data:
                tmp += 1
        if tmp == 1:
            cnt += 1

    print(cnt)


class Graph:
    def __init__(self, v, e) -> None:
        """
        v : 頂点
        e : 辺
        """
        self.v = v
        self.e = e
        self.edge = [[] for _ in range(self.v)]

    def append_edge(self, a, b) -> None:
        self.edge[a - 1].append(b - 1)
        self.edge[b - 1].append(a - 1)

    def bfs(self, first=0) -> list:
        from collections import deque
        from math import inf

        dist = [inf] * self.v
        root = [inf] * self.v
        q = deque()

        dist[first] = 0

        q.append(first)
        while len(q) != 0:
            before_id = q.popleft()
            for next_v in self.edge[before_id]:
                if dist[next_v] != inf:
                    continue
                else:
                    root[next_v] = before_id
                    dist[next_v] = dist[before_id] + 1
                    q.append(next_v)
        return dist, root

    def is_star(self) -> bool:
        for i, num in enumerate(self.edge):
            if len(self.edge[i]) == self.e:
                return True
        return False


if __name__ == "__main__":
    main()
