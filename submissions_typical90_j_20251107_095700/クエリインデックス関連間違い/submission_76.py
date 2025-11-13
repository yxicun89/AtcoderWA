n=int(input())
a=[]
b=[]

for i in range(n):
  c,p=map(int,input().split())
  if c == 1:
    a.append(p)
    b.append(0)
  else:
    a.append(0)
    b.append(p)
sa=[0]*(len(a)+1)
sb=[0]*(len(b)+1)
sa[1]=a[0]
sb[1]=b[0]
for i in range(1,len(a)):
  sa[i]=sa[i-1]+a[i]
for i in range(1,len(b)):
  sb[i]=sb[i-1]+b[i]

q=int(input())
for _ in range(q):
  l,r=map(int,input().split())
  print(sa[r-1]-sa[l-2],sb[r-1]-sb[l-2])