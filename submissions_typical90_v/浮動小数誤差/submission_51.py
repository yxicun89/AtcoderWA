import math

#データ入力
A, B, C = map(int,input().split(" "))

#データ処理
g = math.gcd(A,B,C)

result = int((A / g - 1) + (B / g - 1) + (C / g - 1))
print(result)

