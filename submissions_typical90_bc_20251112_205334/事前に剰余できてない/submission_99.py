N,P,Q=map(int,input().split())
A=list(map(int,input().split()))
aa=[]
ans=0
for i in A:
    aa.append(i%P)
for i in range(N-4):
    for j in range(i+1,N-3):
        for k in range(j+1,N-2):
            for l in range(k+1,N-1):
                for m in range(l+1,N):
                    if i*j*k*l*m%P==Q:
                        ans+=1
print(ans)