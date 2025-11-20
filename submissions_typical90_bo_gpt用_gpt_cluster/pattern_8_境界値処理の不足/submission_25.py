N, K = map(int, input().split())
N = str(N)

for i in range(K):
    # 8進法を10進法に変換
    val = 0
    for j in range(1, len(N) + 1):
        val += int(N[-j]) * int(8 ** (j - 1))

    s = []
    # 10進法を9進法に変換
    while val > 0:
        q = val % 9
        val //= 9

        s.append(str(q))
    # 9進法の文字列から8を5に変換
    s = "".join(reversed(s))
    N = s.replace("8", "5")

print(N)
