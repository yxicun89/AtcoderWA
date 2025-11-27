A,B,C=map(int,input().split())

import math

D=math.gcd(A,B,C)

sum=((A+B+C)/D)-3

print(int(sum))