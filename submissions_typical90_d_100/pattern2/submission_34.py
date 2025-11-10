H,W = map(int,input().split())

A=[]*W
B=[0]*H
C=[0]*W
for i in range(H):
  A.append(list(map(int,input().split())))
  B[i] = sum(A[i])

  for j in range(W):
    C[j] = A[i][j]+C[j]

P=[0]*W
for i in range(H):
  for j in range(W):
    P[j]=str(B[i]+C[j])
    
  print(" ".join(P))