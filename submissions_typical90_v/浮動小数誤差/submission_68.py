import math
a,b,c = map(int, input().split())
d = math.gcd(a,b,c)
total = int(a/d)+int(b/d)+int(c/d)-3
print(total)