# インデックスずれ
N = int(input())
C = [0]
P = [0]
for i in range(N):
    c, p = map(int, input().split())
    C.append(c)
    P.append(p)

P1 = [0]
P2 = [0]
S1_sum = 0
S2_sum =0

for i in range(N):
    if C[i] == 1:
        S1_sum += P[i]
    else:
        S2_sum += P[i]
    P1.append(S1_sum)
    P2.append(S2_sum)
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(f"{P1[r] - P1[l-1]} {P2[r] - P2[l-1]}")
