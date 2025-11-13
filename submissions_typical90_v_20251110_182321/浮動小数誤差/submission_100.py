import math
A=list(map(int,input().split()))
gcd=math.gcd(A[0],A[1],A[2])
sum=(((A[0]/gcd)-1)+((A[1]/gcd)-1)+((A[2]/gcd)-1))

print(int(sum))