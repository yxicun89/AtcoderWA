n,p,q = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      for l in range(k+1,n):
        for m in range(l+1,n):
          if i*j%p*k%p*l%p*m % p == q:
            c += 1

print(c)