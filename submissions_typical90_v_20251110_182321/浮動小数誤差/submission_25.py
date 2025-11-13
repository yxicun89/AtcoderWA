import math
a, b, c = list(map(int, input().split()))
print(int((a+b+c)/math.gcd(a, b, c)-3))