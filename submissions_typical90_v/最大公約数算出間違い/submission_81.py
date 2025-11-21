A,B,C=map(int,input().split())
#print(A,B,C)
D=max(A,B,C)-min(A,B,C)
#print(D)
m=min(A,B,C,D)
#print(m)
def check(M):
  if A%M==0 and B%M==0 and C%M==0:
    return True
  else:
    return False

L,R=1,m    
while L!=R:
  M=(L+R)//2+1
  if check(M)==True:
    L=M
  else:
    R=M-1

A//=L
B//=L
C//=L
print(A+B+C-3)