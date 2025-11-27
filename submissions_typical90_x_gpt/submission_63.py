import math
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
num=0
      
for i in range(N):
  if(A[i]!=B[i]):
    num=abs(A[i]-B[i])
    K-=num

if((K<0) or (K%2!=0)):
  print("No")
else:
  print("Yes")

print(N,K)
print(A)
print(B)