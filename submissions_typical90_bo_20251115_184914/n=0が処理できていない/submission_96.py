N, K = map(int, input().split())

def convert_10(N):
    num = 0
    i = 0
    while N > 0:
        keta = N % 10
        num += keta * (8 ** i)
        N //= 10
        i += 1
    return num  # 10進数

def convert_9(num):
    kotae = []
    while num > 0:
        t = num % 9
        if t == 8:
            t = 5
        kotae.append(t)
        num //= 9
    if not kotae:
        kotae.append(0)
    kotae.reverse()
    result = ''.join(map(str, kotae))
    return int(result)

def convert_back_to_8(num):
    result = 0
    power = 1
    while num > 0:
        result += (num % 10) * power
        num //= 10
        power *= 9
    return result

for _ in range(K):
    num_in_10 = convert_10(N)
    num_in_9 = convert_9(num_in_10)
    N = convert_back_to_8(num_in_9)

print(N)