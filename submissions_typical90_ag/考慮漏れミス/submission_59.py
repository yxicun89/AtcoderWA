# 高さと横幅が偶数の場合は、2x2のブロックの個数を計算する
#

h, w = map(int, input().split())

if h % 2 == 0 and w % 2 == 0:
    print((h // 2) * (w // 2))
elif h % 2 == 0 and w % 2 == 1:
    print((h // 2) * ((w // 2) + 1))
elif h % 2 == 1 and w % 2 == 0:
    print(((h // 2) + 1) * (w // 2))
else:
    print(((h // 2) + 1) * ((w // 2) + 1))