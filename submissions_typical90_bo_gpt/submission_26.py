def eton(X):
  Y = list(X)
  Y.reverse()
  a = 0
  for i in range(len(Y)):
    a += int(Y[i])*8**i
  Z = []
  while a != 0:
    if a % 9 == 8:
      Z.append(5)
    else:
      Z.append(a%9)
    a = a // 9
  Z.reverse()
  k = ""
  for i in range(len(Z)):
    k += str(Z[i])
  return k
N, K = map(int, input().split())
P = str(N)
for i in range(K):
  P = eton(P)
print(P)