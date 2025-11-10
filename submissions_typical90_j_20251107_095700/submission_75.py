N = int(input())
C = [0 for _ in range(N)]
P = [0 for _ in range(N)]
for i in range(N):
    C[i], P[i] = map(int,input().split())
Q = int(input())
L = [0 for _ in range(Q)]
R = [0 for _ in range(Q)]
for i in range(Q):
    L[i], R[i] = map(int,input().split())

sum = [[0 for _ in range(N)] for _ in range(2)]


for i in range(N):
    if (i == 0):
        sum[C[i]-1][i] = P[i]
    if (C[i] == 1):
        sum[0][i] = sum[0][i-1] + P[i]
        sum[1][i] = sum[1][i-1]
    else:
        sum[1][i] = sum[1][i-1] + P[i]
        sum[0][i] = sum[0][i-1]

ans1 = []
ans2 = []
for i in range(Q):
    if(L[i] == 1):
        ans1.append(sum[0][R[i]-1])
        ans2.append(sum[1][R[i]-1])
    else:
        ans1.append(sum[0][R[i]-1] - sum[0][L[i]-2])
        ans2.append(sum[1][R[i]-1] - sum[1][L[i]-2])
for i in range(Q):
    print(ans1[i],ans2[i])