N,M=map(int,input().split())
d={}
for i in range(M):
    a,b=map(int,input().split())
    if a not in d:d[a]=[]
    if b not in d:d[b]=[]
    d[a].append(b)
    d[b].append(a)
cnt=0
for i in d:
    if len(d[i])>1:continue
    if d[i][0]<i:cnt+=1
print(cnt)