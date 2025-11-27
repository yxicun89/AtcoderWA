x, y, z = map(int,input().split())



import math



# 2つの数の最大公約数

g = math.gcd(x, y, z)

ans = int((x+y+z)/g)-3

print(int(ans))
