import math
A,B,C=list(map(int,input().split()))
gcd=(math.gcd(A, B, C))

if(gcd!=1):
  cnt=int(math.log(A,gcd))+int(math.log(B,gcd))+int(math.log(C,gcd))-3
else:
  cnt=A+B+C-3
print(cnt)