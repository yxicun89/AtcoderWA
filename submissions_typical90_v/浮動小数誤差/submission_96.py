import math
l = list(map(int, input().split()))

gcd = math.gcd(l[0],math.gcd(l[1],l[2]))
ans =((l[0]/gcd)-1)+((l[1]/gcd)-1)+((l[2]/gcd)-1)
print(int(ans))