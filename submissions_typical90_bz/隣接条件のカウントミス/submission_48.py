import itertools
N, M = map(int, input().split())

d = [0]*N
for i in range(M):
  a,b = map(int, input().split())
  a -= 1
  b -= 1
  if(a<b):
    d[a] += 1
  if(b>a):
    d[b] += 1


print(d.count(1))