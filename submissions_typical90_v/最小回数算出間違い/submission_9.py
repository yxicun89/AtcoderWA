import math

A,B,C = map(int,input().split())

n = math.gcd(A,B,C)

print((A+B+C//n)-3)
