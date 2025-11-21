from itertools import combinations
a,b,c=map(int,input().split())
e=list(map(int,input().split()))
for i in range(a):
  e[i]=e[i]%b
f=list(combinations(e,5))
h=0
g=float("inf")
for i in range(len(f)):
  if sum(f[i])%b==c:
    h+=1
print(h)