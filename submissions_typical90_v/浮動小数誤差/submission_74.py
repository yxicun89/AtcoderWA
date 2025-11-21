# -*- coding: utf-8 -*-
import math

# 整数の入力
a, b, c = map(int, input().split())

# 立方体の体積
v = a*b*c

# 最大公約数（立方体の一辺の長さに相当）
gcd = math.gcd(math.gcd(a, b), c)

# 立方体の個数
n = v/(gcd**3)

count = int(a/gcd - 1) + int(b/gcd - 1) + int(c/gcd - 1)

print(count)
