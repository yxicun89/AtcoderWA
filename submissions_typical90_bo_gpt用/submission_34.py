N,K=input().split()
K=int(K)

for _ in range(K):
  a=0
  for n in N:a=a*8+int(n)
  s=""
  while a>0:
    if a%9==8:
      s=str(5)+s
    else:s=str(a%9)+s
    a//=9
  N=s
print(N)