#累積和の初期化間違い

#入力
N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]

#クラスごとにiさんの点数リストをつくる
P_C1 = [0] * N
P_C2 = [0] * N
for i in range(N):
    if CP[i][0] == 1:
        P_C1[i] = CP[i][1]

    else:
        P_C2[i] = CP[i][1]

#累積和に
S_C1 = [0] * N
S_C2 = [0] * N
for i in range(N):
    if i == 0:
        S_C1[i] = P_C1[i]
        S_C2[i] = P_C2[i]

    S_C1[i] = S_C1[i - 1] + P_C1[i]
    S_C2[i] = S_C2[i - 1] + P_C2[i]

#答え
Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    if L == 0:
        A = S_C1[R]
        B = S_C2[R]
    else:
         A = S_C1[R] - S_C1[L - 1]
         B = S_C2[R] - S_C2[L - 1]

    print(A, B)
