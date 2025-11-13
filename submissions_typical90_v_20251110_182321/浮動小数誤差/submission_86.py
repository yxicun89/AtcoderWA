import math

A,B,C = map(int,input().split())

result = -3

result += A / math.gcd(A,B,C)

result += B / math.gcd(A,B,C)

result += C / math.gcd(A,B,C)

print(result)