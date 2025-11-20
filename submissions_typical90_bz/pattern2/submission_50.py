from collections import defaultdict
from heapq import *
N,M=map(int,input().split())
li=[[] for i in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    heappush(li[a-1],b-1)
    heappush(li[b-1],a-1)
c=0
for i in range(N):
    if len(li[i])>1:
        if li[i][0]<i and li[i][1]>=i:
            c+=1
    else:
        if li[i][0]<i:
            c+=1
print(c)