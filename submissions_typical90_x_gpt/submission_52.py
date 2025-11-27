# -*- coding:utf-8 -*-

n, k = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

for i in range(n):
    k -= abs(a[i]-b[i])

if k % 2 == 1:
    print("No")
else:
    print("Yes")