# 入力
H, W = map(int, input().split())

# Hが偶数の場合はH//2が縦の最大、偶数の場合はH//2+1が縦の最大
# Wが偶数の場合はW//2が縦の最大、偶数の場合はW//2+1が縦の最大

if H % 2 == 0:
    if W % 2 == 0:
        max_led = (H // 2)*(W // 2)
    else:
        max_led = (H // 2)*(W // 2 + 1)
else:
    if W % 2 == 0:
        max_led = (H // 2 + 1)*(W // 2)
    else:
        max_led = (H // 2 + 1)*(W // 2 + 1)

# 出力
print(max_led)