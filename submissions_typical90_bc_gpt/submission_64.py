n,p,q = map(int,input().split())
x = list(map(int,input().split()))
ans = 0
#5重ループは無理かと思いきや1/120されてるから大丈夫
# 膨大な数になるのを防ぐために各余りとってる
for a in range(n):
  for b in range(a+1,n):
    for c in range(b+1,n):
      for d in range(c+1,n):
        for e in range(d+1,n):
          y = 0
          y += x[a] % p
          y += x[b] % p
          y += x[c] % p
          y += x[d] % p
          y += x[e] % p
          if (y % p) == q:
            ans += 1
            
print(ans)   