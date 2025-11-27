N,M=map(int,input().split())
dic={}
for _ in range(M):
    a,b=map(int,input().split())
    dic.setdefault(a,[])
    dic[a].append(b)
    dic.setdefault(b,[])
    dic[b].append(a)
ans=0
for i in range(1,N+1):
    count=0
    if dic.get(a)==None:
        continue
    for d in dic.get(a):
        if d <i:
            count+=1
    if count==1:
        ans+=1
print(ans)
    