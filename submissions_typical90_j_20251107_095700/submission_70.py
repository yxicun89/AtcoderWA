N = int(input())
C1sum = [0] * N
C2sum = [0] * N
sum1 = 0
sum2 = 0
for i in range(N):
    C, P = map(int,input().split())
    if C == 1:
        sum1 += P
    else:
        sum2 += P
    C1sum[i] = sum1
    C2sum[i] = sum2

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    p1 = C1sum[R - 1] - C1sum[L - 2]
    p2 = C2sum[R - 1] - C2sum[L - 2]
    print(p1, p2)
    