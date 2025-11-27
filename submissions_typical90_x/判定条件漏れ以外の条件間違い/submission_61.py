import sys
N,K=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))
d=0
for i in range(N):
  d+=abs(A[i]-B[i])
if K>d and (K-d)%2==0:
  print("Yes")
else:
  print("No")