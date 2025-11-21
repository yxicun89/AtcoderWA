n = int(input())

c1 = []
c2 = []
for i in range(n):
  c, s = map(int, input().split())
  if c == 1:
    c1.append(s)
    c2.append(0)
  else:
    c1.append(0)
    c2.append(s)

q = int(input())

for j in range(q):
  f, t = map(int, input().split())
  print("{} {}".format(sum(c1[f:t]),sum(c2[f:t])))