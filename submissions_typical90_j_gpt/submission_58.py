N = int(input())

c1 = [0]*N
c2 = [0]*N

for n in range(N):
  c,p = map(int, input().split())
  if c == 1:
    c1[n] = p
  else:
    c2[n] = p

s1 = [0]*(N+1)
s2 = [0]*(N+1)

for i in range(N):
  s1[i+1] = s1[i] + c1[i]
  s2[i+1] = s1[i] + c2[i]

Q = int(input())

for _ in range(Q):
  l, r = map(int, input().split())
  sum1 = s1[r] - s1[l-1]
  sum2 = s2[r] - s2[l-1]
  print(sum1, sum2)