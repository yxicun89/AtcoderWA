# 次使うnを更新していない

def base8_to_10(s: str) -> int:

    res = 0

    for ch in s:

        res = res * 8 + int(ch)

    return res



def base10_to_9(num: int) -> str:

    if num == 0:

        return "0"

    res = ""

    while num > 0:

        res = str(num % 9) + res

        num //= 9

    return res



n, k = input().split()

k = int(k)



for _ in range(k):

    n10 = base8_to_10(n)

    n9 = base10_to_9(n10)

    ans = n9.replace("8", "5")



print(ans)
