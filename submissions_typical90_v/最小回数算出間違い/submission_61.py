import math

a,b,c = map(int,input().split(" "))

kouyakusuu = math.gcd(a,b,c)

print(a//kouyakusuu + b//kouyakusuu + c//kouyakusuu)
