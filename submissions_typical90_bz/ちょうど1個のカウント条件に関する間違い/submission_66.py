N, M = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(M)]
L = [] 

for i in range(M): 

  if A[i][0] < A[i][1]:
    if A[i][1] in L:
      L.remove(A[i][1])
    else:
      L.append(A[i][1])
  elif A[i][0] > A[i][1]:
    if A[i][0] in L:
      L.remove(A[i][0])
    else:
      L.append(A[i][0])

print(len(L))