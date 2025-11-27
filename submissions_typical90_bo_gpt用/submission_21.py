
def to_base9(n: int) -> str:

    if n == 0:

        return "0"

    digit = ""

    while n:

        digit = str(n % 9) + digit

        n //= 9

    return digit



N, K = map(int, input().split())

# 最初のNは8進数として解釈する

n = int(str(N), 8)



for _ in range(K):

    s = to_base9(n)

    s = s.replace("8", "5")

    n = int(s)  # ここは整数として保持しておく



print(s)

