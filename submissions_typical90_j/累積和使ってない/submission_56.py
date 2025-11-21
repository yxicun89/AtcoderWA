N = int(input())
C = [None] * N
P = [None] * N

for i in range(N):
    C[i], P[i] = map(int, input().split(' '))

Q = int(input())
L = [None] * Q
R = [None] * Q

for i in range(Q):
    output = [0]*2
    L[i], R[i] = map(int, input().split(' '))
    for j in range(L[i]-1, R[i]):
        output[C[j]-1] += P[j]
    print(output)