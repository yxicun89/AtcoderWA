N, M = map(int, input().split())
ans=0
G = {} # 隣接リストを表す辞書
for i in range(1, N+1):
  G[i] = set() # 頂点iに隣接する頂点の集合

for i in range(1, M+1):
  A, B = map(int, input().split())
	# 無向グラフなので、両方向に辺を張る
  G[A].add(B)
  G[B].add(A)
a=[]
for i in range(N):
  a.append(list(G[i+1]))
for i in range(N):
  if len(a[i])==1 and a[i][0]<i+1:
    ans+=1
  elif a[i][0]<i+1 and a[i][1]>=i+1:
    ans+=1
print(ans)