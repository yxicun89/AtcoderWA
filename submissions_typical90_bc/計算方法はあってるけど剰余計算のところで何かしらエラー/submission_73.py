n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i1 in range(n):
  p1 = a[i1]
  for i2 in range(i1,n):
    p2 = p1 * a[i2] % p
    for i3 in range(i2, n):
      p3 = p2 * a[i3] % p
      for i4 in range(i3, n):
        p4 = p3 * a[i4] % p
        for i5 in range(i4, n):
          if p4 * a[i5] % p == q:
            ans += 1
print(ans)
