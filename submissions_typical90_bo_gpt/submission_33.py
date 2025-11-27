N, K = map(int, input().split())

n = str(N)
for i in range(K):

    m = 1
    total = 0
    for i in range(len(n)):
        total += int(n[-m]) * 8 ** (i)
        m += 1

    S = ""
    while total > 0:
        S = str(total % 9) + S
        total = total // 9

    n = S.replace("8", "5")

print(n)