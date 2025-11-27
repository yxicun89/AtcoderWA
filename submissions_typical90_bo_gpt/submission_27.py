n,k=map(int,input().split())
m=str(n)
n=[int(m[i]) for i in range(len(m))]
def f(n):
  n10=0
  i=0
  while n:
    n10+=n[-1]*(8**i)
    i+=1
    n=n[:-1]
  n9=[]
  while n10>8:
    n9=[n10%9]+n9
    n10=n10//9
  n9=[n10]+n9
  n8=[5 if i==8 else i for i in n9]
  return n8

for i in range(k):
  n=f(n)
a=0
for i in range(len(n)):
  a+=n[i]*(10**i)
print(a)