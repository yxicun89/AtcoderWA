# 最大公約数計算間違い

a, b, c = map(int, input().split())

l = sorted([a,b,c])
x,y,z = l
if y % x == 0 and z % x == 0:
    y //= x
    z //= x
    x = 1

ans = (x + y + z) - 3
print(ans)
