import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
edge,node=[[] for n in range(N)],[-1]*N
for m in range(M):
    a,b = map(int,input().split())
    if a>b :edge[a-1].append(b-1)
    if b<a :edge[b-1].append(a-1)
ans = 0
for n in range(N):
    if len(edge[n])==1:ans+=1
print(ans)