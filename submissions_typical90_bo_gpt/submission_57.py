N, K = input().split()
K = int(K)
for i in range(K):
    n = 0
    for j in range(len(N)):
        b8 = int(N[-1-j])*(8**j)
        # print(i, j, N[-1-j], (8**j), b8)
        n += b8
    # print(i, n)
    N = ''
    while n>0:
        b9 = n%9
        if b9 == 8:
            N = '5' + N
        else:
            N = str(b9) + N
        n = n // 9
    # print(i, N)
print(N)
