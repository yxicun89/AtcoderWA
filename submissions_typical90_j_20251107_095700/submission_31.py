N = int(input())
S1 = [0]*N
S2 = [0]*N
temp1 = 0
temp2 = 0
for i in range(N) :
  C, P = map(int, input().split())
  if C == 1 :
    temp1 += P
  else :
    temp2 += P
  S1[i] = temp1
  S2[i] = temp2
Q = int(input())
for i in range(Q) :
  L, R = map(int, input().split())
  L -= 1
  R -= 1
  if L == 0 :
    A = S1[R]
    B = S2[R]
  else :
    A = S1[R] - S1[L-1]
    B = S2[R] - S1[L-1]
  print(A, B)