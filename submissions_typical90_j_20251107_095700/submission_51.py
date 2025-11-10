N = int(input())
A = []
B = []
add_A,add_B = 0,0
for _ in range(N):
  C,P= [int(x) for x in input().split()]
  if C == 1:
    add_A += P
    A.append(add_A)
    B.append(add_B)
  else:
    add_B += P
    A.append(add_A)
    B.append(add_B)
Q = int(input())
for _ in range(Q):
  L,R = [int(x) for x in input().split()]
  print(A[R-1]-A[L-2],B[R-1]-B[L-2])