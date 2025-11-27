import math
A = list(map(int,input().split()))
D=math.gcd(A[0], A[1], A[2])
print(int(A[0]/D-1)+int(A[1]/D-1)+int(A[2]/D-1))