import math
a,b,c=map(int,input().split())
k=math.lcm(a,b,c)
print((k//a +k//b+k//c)-2)