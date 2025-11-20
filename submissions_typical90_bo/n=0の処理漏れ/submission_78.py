def f(x):
    x = x[: : -1]
    tmp = 0
    for i in range(len(x)):
        tmp += 8**i * int(x[i])
    y = ""
    while tmp:
        q, r = divmod(tmp, 9)
        tmp = q; y += str(r)
    y = y[: : -1]
    y = y.replace("8", "5")
    return y


N, K = input().split()

for _ in range(int(K)):
    N = f(N)

print(N)
