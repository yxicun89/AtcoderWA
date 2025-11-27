
Q = int(input())

s = []

ans = []



for i in range(Q):

  t,x = map(int,input().split())

  if t == 1:

    s.append(x)

  if t == 2:

    s.insert(0,x)

  if t == 3:

    ans.append(s[x-1])

for a in ans:

  print(a)
