import math

# 直方体を分割し、立方体を作る場合、立方体の一辺の長さは、直方体の各辺の最大公約数になる。
A, B, C = map(int, input().split())

# 最大公約数を d とする
d = math.gcd(A, B, C)

times_cut = (A/d - 1) + (B/d - 1) + (C/d - 1)
print(times_cut)