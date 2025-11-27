a, b, c = map(int, input().split())
s = 1
for i in range(1, min(a,b,c)):
  if (a % i == 0) and (b % i == 0) and (c % i == 0):
    s = i
k = a / s - 1
l = b / s - 1
m = c / s - 1
print(k + l + m)