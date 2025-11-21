import time

n,P,q=map(int,input().split())
a=list(map(int,input().split()))
s=time.time()
ans=0
for i in range(n-4):
    for j in range(i+1,n-3):
        for k in range(j+1,n-2):
            for l in range(k+1,n-1):
                for m in range(l+1,n):
                    if (((((((i*j)%P)*k)%P)*l)%P)*m)%P==q:
                        ans+=1
g=time.time()
# print(g-s)
print(ans)