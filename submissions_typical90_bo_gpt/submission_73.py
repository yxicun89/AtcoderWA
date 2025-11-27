N, K = map(int, input().split())
N = str(N)

for _ in range(K):
    ret = 0
    for n in N:
        ret *= 8
        ret += int(n)
    ans = ''
    while ret:
        ret, r = divmod(ret, 9)
        if r == 8:
            r = 5
        ans += str(r)
    ans = ans[::-1]
    N = ans
print(ans)