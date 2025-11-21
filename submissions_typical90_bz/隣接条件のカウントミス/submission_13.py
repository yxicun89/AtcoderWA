N,M=map(int,input().split())
A=[]
B=[]

for i in range(M):
  a,b =map(int,input().split())
  A.append(a)
  B.append(b)
  
for j in range(M):
  if A[j]>B[j]:
   C=A[j]
   A[j]=B[j]
   B[j]=C
  Bs=sorted(B)
x=0
for j in range(N):
  if Bs.count(i)==1:
    x+=1
print(x)
