def change_10_from_8(N):
    # 8進数を10進数に変換する
    str_N = N
    rst = 0
    i = 0
    for n in str_N[::-1]:
        rst += int(n) * (8 ** i)
        i += 1
    return rst

def change_9_from_10(N):
    rst = ""
    while N > 0:
        rst += str(N % 9)
        N //= 9
    return rst[::-1]

N, K = input().split()
for k in range(int(K)):
    n = change_10_from_8(N)
    m = change_9_from_10(n)
    m = m.replace("8", "5")
    N = m
print(N)
