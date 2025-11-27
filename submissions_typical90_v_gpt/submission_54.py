import math
cake = list(map(int, input().split()))

ans = 0
cube_henn = math.gcd(cake[0], cake[1], cake[2])

for i in range (3):
  ans += cake[i] // cube_henn
print(ans)