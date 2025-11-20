n,k=input().split()
for i in range(int(k)):
  t=0
  for j in range(1,len(n)+1):
    t+=int(n[-j])*8**(j-1)
  a=[]
  while t>0:
    s=t%9
    if s==8:
      s=5
    a.append(str(s))
    t//=9
  a.reverse()
  n=''.join(a)
print(n)