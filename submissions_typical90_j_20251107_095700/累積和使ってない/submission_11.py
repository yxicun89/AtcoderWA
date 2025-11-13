# 累積和使ってない
N = int(input())
lst_a = []
for _ in range(N):
  a, b = map(int, input().split())
  lst_a.append([a, b])
  
Q = int(input())
lst_b = []
for _ in range(Q):
  a, b = map(int, input().split())
  lst_b.append([a, b])

for L, R in lst_b:
  total_A = 0
  total_B = 0
  for i in range(L, R+1):
    if lst_a[i-1][0] == 1:
      total_A += lst_a[i-1][1]
    else:
      total_B += lst_a[i-1][1]

print(total_A, total_B)