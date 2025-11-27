
# K-最低必要回数が偶数なら可能



N,K = map(int,input().split())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

A.sort()

B.sort()



cont = 0

for i in range(N):

  cont += abs(A[i]-B[i])



if K-cont >= 0 and (K-cont)%2 == 0:

  print("Yes")

else:

  print("No")
