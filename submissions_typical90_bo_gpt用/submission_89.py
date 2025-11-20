N, K = map(int, input().split())
S = str(N)

for _ in range(K):
  i = sum(int(s) * (8 ** i) for i, s in enumerate(reversed(S)))
  
  S = ""
  while i > 0:
    j = i % 9
    S += str(j if j != 8 else 5)
    i //= 9
  S = S[::-1]
  
print(S)
