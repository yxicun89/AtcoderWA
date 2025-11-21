N, M = map(int, input().split())
AB = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)] # 0-indexed

# 隣接リスト表現
G = [[] for _ in range(N)]
for a, b in AB:
    G[a].append(b)
    G[b].append(a)

# 自分より小さいノードへの辺がちょうど1つ
ans = sum([1 if len(edges) == 1 else 0 for edges in G])
print(ans)