n,p,q=map(int,input().split())
a=list(map(int,input().split()))
ans=0

for i in range(n-4):
  xi=a[i]%p
  for j in range(i+1,n-3):
    xj=xi*(a[j]%p)
    for k in range(j+1,n-2):
      xk=xj*(a[k]%p)
      for l in range(k+1,n-1):
        xl=xk*(a[l]%p)
        for m in range(l+1,n):
          if xl*(a[m]%p)==q:
            ans+=1

print(ans)