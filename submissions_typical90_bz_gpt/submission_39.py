N,M=map(int,input().split())
Shl=[[] for i in range(N+1)]
#print(Shl)
for i in range(M):
    A,B=map(int,input().split())
    Shl[A].append(B)
    Shl[B].append(A)
ans=0
#print(Shl)
for i in range(1,N+1):
    cnt=0
    for j in range(len(Shl[i])):
        if j<i:
            cnt +=1
        else:
            pass
    if cnt==1:
        ans+=1
print(ans)