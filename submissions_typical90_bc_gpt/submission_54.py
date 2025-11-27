N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

atta = 0
for u in range(N):
  z = A[u]
  for v in range(u+1, N):
    z = (z*A[v])%P
    for w in range(v+1, N):
      z = (z*A[w])%P
      for x in range(w+1, N):
        z = (z*A[x])%P
        for y in range(x+1, N):
          if (z*A[y])%P==Q: atta += 1 

print(atta)