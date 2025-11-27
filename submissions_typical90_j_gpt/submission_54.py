
N = int(input())
ten_1 = [0] * (N+1)
ten_2 = [0] * (N+1)
#学籍番号a番の ten[a]
for _ in range(N):
  k = list(map(int,input().split()))
  if k[0] == 1:
    ten_1[_] = k[1]
  else:
    ten_2[_] = k[1]

t_1 = ten_1
t_2 = ten_2
for _ in range(N):
  t_1[_+1] = t_1[_] + t_1[_+1]
  t_2[_+1] = t_2[_] + t_2[_+1]


Q = int(input())
l = []
r = []
for _ in range(Q):
  k = list(map(int,input().split()))
  l.append(k[0])
  r.append(k[1])

# print(ten_1)
# print(ten_2)
# print(l,r)
for _ in range(Q):
  a = t_1[r[_]] - t_1[l[_]-1]
  b = t_2[r[_]] - t_2[l[_]-1]
  print(a,b)
