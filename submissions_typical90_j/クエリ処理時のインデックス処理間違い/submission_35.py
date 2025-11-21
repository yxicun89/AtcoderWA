n = int(input())
c, p = [0] * n, [0] * n
for i in range(n):
  c[i], p[i] = map(int, input().split())
  
one = [0] * (n + 1)
two = [0] * (n + 1)

for i in range(n):
  one[i + 1] += one[i]
  two[i + 1] += two[i]
  
  if c[i] == 1:
    one[i + 1] += p[i]
  else:
    two[i + 1] += p[i]

q = int(input())
for i in range(q):
  l, r = map(int, input().split())
  print(one[r] - one[l - r], two[r] - two[l - 1])