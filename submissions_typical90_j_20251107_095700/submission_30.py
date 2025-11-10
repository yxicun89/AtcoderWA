# 入力
C = []
P = []
L = []
R = []

N = int(input())
for i in range(N):
    c , p = map(int, input().split())
    C = C + [c]
    P = P + [p]
    
Q = int(input())
for i in range(Q):
    l , r = map(int, input().split())
    L = L + [l]
    R = R + [r]

sum_L = 0
sum_R = 0

for j in range(Q):
    for i in range(L[j]-1, R[j]):
        if C[i] == 1:
            sum_L = sum_L + P[i]
        else:
            sum_R = sum_R + P[i]
    print(sum_L,sum_R)
