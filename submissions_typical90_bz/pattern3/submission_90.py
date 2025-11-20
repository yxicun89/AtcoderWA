import sys
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())

# 0からnまでのedgeを作成
# 中には隣接するedge番号を入れる
edge = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

# 自分自身より頂点番号が小さい隣接頂点の数を記録
ans = [-1] * (n+1)

def dfs(tgt: int):
    ans[tgt] = 0
    for x in edge[tgt]:
        if x < tgt:
            ans[tgt] += 1
        if ans[x] > 0:
            continue
        dfs(x)

dfs(a)

result = list(filter(lambda x: x == 1, ans))

print(len(result))
