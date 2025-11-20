N,K = map(int,input().split())
N = str(N)
for _ in range(K):
    tens = 0
    tmp = 1
    for i in range(1,len(N)+1):
        tens += tmp * int(N[(-1)*i])
        tmp *= 8
    ans = ""
    while tens:
        ans = str(tens%9) + ans
        tens //= 9
    transed = ""
    for i in range(len(ans)):
        if ans[i] == "8":
            transed = transed + "5"
        else:
            transed = transed + ans[i]
    N = transed

print(N)