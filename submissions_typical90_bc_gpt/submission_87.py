n,p,q = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
for i1 in range(n):
  for i2 in range(i1+1,n):
    for i3 in range(i2+1,n):
      for i4 in range(i3+1,n):
        for i5 in range(i4+1,n):
          if (a[i1]%p+a[i2]%p+a[i3]%p+a[i4]%p+a[i5]%p)%p == q:
            ans += 1

print(ans)