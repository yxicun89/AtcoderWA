n, p, q = map(int,input().split())
a = list(map(lambda x:int(x)%p,input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                for m in range(l+1,n):
                    if (i*j*k*l*m)%p == q:
                        ans += 1
print(ans)