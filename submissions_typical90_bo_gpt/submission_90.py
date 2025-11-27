def base8_to_int(S:str):
    ans = 0
    for i in range(0, len(S)):
        now = int(S[len(S)-1-i])
        ans += now*8**i
    return ans

def int_to_base9(n:int):
    ans = ""
    while n != 0:
        tmp = n % 9
        ans = str(tmp) + ans
        n = n // 9
    return ans

    

N,K = input().split()
K = int(K)
next_str = N
for _ in range(K):
    num = base8_to_int(next_str)
    nine_str = int_to_base9(num)
    next_str = nine_str.replace("8", "5")

print(next_str)