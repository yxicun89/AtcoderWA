Q = int(input())
T = []
X = []

for i in range(Q):
  t, x = list(map(int,input().split()))
  T.append(t)
  X.append(x)

for i in range(Q):
  if T[i] == 1:
    X.insert(0, X[i])
  
  if T[i] == 2:
    X.insert(Q-1, X[i])

  if T[i] == 3:
    print(X[i])