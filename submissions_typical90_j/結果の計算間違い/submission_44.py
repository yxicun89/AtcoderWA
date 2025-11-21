# 結果の計算違い
# H, W = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(H)]
# B = [[0]*W for _ in range(H)]

# s_h = [0]*W
# s_w = [0]*H

# for i in range(W):
#     for j in range(H):
#         s_h[i] += A[j][i]
# for i in range(H):
#     s_w[i] = sum(A[i])

# # print(s_h, s_w)
# for i in range(H):
#     for j in range(W):
#         B[i][j] = (s_h[j]+s_w[i]-A[i][j])

# for i in range(H):
#     print(*B[i])

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
A_P = [0]*N
B_P = [0]*N
for i in range(N):
    if P[i][0]==1:
        A_P[i] = P[i][1]
    else:
        B_P[i] = P[i][1]
DA = A_P.copy()
DB = B_P.copy()
for i in range(1,N):
    DA[i] += DA[i-1]
    DB[i] += DB[i-1]
# print(A_P,DA , B_P,DB)
Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    print(DA[R]-DA[L]+A_P[L], DB[R]-DB[L]+A_P[L])
    # print(A_P[L:R],B_P[L:R])
