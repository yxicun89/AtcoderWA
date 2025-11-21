import math

cake = list(map(int, input().split()))

m = math.gcd(cake[0], math.gcd(cake[1], cake[2]))

ans = 0
for p in cake:
  ans += p / m - 1

print(int(ans))