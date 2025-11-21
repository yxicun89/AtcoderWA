import math
A,B,C = map(int,input().split())
a = int(A / math.gcd(A,B,C))
b = int(B / math.gcd(A,B,C))
c = int(C / math.gcd(A,B,C))
print(a + b + c - 3)