import math
from functools import reduce

# 入力の読み込み
cake = list(map(int, input().split()))

# 3つの最大公約数を求める
result = reduce(math.gcd, cake)

# 切る回数を求める
cnt = 0
for i in range(len(cake)):
    cnt += (cake[i] / result) - 1

# 出力
print(int(cnt))


