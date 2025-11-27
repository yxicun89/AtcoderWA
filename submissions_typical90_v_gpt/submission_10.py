import math 

a,b,c = map(int, input().split())

d = math.gcd(a,b,c)

print(a//d+b//d+c//d)