import bisect

n,m=map(int,input().split())

arm=[[]*n for _ in range(n) ]

ans=0

for i in range(m):

  a,b=map(int,input().split())

  arm[a-1].append(b-1)

  arm[b-1].append(a-1)



for i in range(len(arm)):

  if bisect.bisect_left(arm[i], i) == 1:

    ans+=1



print(ans)



