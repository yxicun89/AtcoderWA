import math
a,b,c = map(int,input().split())
common_divisor = math.gcd(a,b,c)
ans = int(a/common_divisor - 1 + b/common_divisor - 1 + c/common_divisor - 1)
print(ans)