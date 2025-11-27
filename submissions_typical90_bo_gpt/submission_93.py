n, k = map(int, input().split())
# print(n, k)
# 8進数を10新数に変換（高速な方法があるかも）
def reconvert(n):
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * (8 ** (len(n) - i - 1))
    return result
        
# 10進数を9新数に変換
def convert(n):
    result = ""
    while n > 0:
        result = str(n % 9) + result
        n //= 9
    return result
    
# 8を5に変換
def eightto5(n):
    result = ""
    for i in range(len(n)):
        if n[i] == "8":
            result = result + "5"
        else:
            result = result + n[i]
        # print(result)
    return result
for _ in range(k):
    n = reconvert(str(n))
    n = convert(int(n))
    n = eightto5(str(n))
print(n)