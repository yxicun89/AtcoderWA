n,p,q = map(int,input().split())
a = list(map(int,input().split()))
count =0
for h in range(n-4):
  for i in range(h,n):
    for j in range(i,n):
      for k in range(j,n):
        for l in range(k,n):
          if (a[h]*a[i]*a[j]*a[k]*a[l])%p==q:
            count +=1
print(count)