# 条件が一致だけ

n,k = map(int,input().split())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

s = 0

for i in range(n): s += abs(a[i] - b[i])

if s == k: print("Yes")

else: print("No")
