
N = int(input())
CPpairs = []
for _ in range(N):
    C,P =map(int, input().split())
    CPpairs.append((C,P))

Q = int(input())
LRpairs = []
for _ in range(Q):
    L,R = map(int, input().split())
    LRpairs.append((L,R))

# C1sum = 0
# C2sum = 0
# for i in range(N):
#     if CPpairs[i][0] == 1:
#         C1sum += CPpairs[i][1]
#     elif CPpairs[i][0] == 2:
#         C2sum += CPpairs[i][1]

C1sum = [0]*(N+1)
C2sum = [0]*(N+1)

for i in range(1,N+1):
    C,P = CPpairs[i-1]
    C1sum[i] = C1sum[i - 1]
    C2sum[i] = C2sum[i - 1]

if C == 1:
    C1sum[i] += P
elif C == 2:
    C2sum[i] += P

for L,R in LRpairs:
    result1 = C1sum[R] - C1sum[L-1]
    result2 = C2sum[R] - C2sum[L-1]

