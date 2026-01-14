# 計算方法間違い

import math

A,B,C = map(int, input().split())

#A,B,Cの最大公約数を求める。
g = math.gcd(math.gcd(A, B), C)

print(max(max(A, B), C)/g)
