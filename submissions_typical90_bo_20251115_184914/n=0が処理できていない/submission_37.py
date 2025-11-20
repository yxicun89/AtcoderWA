N,K = input().split()
K = int(K)
for _ in range(K):
    tmp = 0
    for c in list(N):
        tmp *= 8
        tmp += int(c)
    N = ''
    while tmp:
        N = str(tmp % 9) + N
        tmp //= 9
    N = N.replace('8', '5')
print(N)