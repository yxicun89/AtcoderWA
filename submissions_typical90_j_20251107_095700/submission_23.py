import sys
N=int(sys.stdin.readline())
sumA=[]
c1,c2=0,0
for i in range(N):
  A,B=map(int,sys.stdin.readline().split())
  if A==1:
    c1+=B
  else:
    c2+=B
  sumA.append([c1,c2])
Q=int(sys.stdin.readline())
for i in range(Q):
  L,R=map(int,sys.stdin.readline().split())
  print(sumA[R-1][0]-sumA[L-2][0],sumA[R-1][1]-sumA[L-2][1])