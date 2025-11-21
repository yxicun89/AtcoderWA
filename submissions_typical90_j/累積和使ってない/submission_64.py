N = int(input())
CP = [map(int,input().split()) for _ in range(N)]
C, P = [list(i) for i in zip(*CP)]
Q = int(input())
LR = [map(int,input().split()) for _ in range(Q)]
L, R = [list(i) for i in zip(*LR)]

Answer1 = 0
Answer2 = 0

for i in range(Q):
    temporaryC = C[L[i]-1:R[i]]
    temporaryP = P[L[i]-1:R[i]]
    c1list = [i for i, x in enumerate(temporaryC) if x == 1]
    for i in range(len(c1list)):
        Answer1 += temporaryP[c1list[i]]
    c2list = [i for i, x in enumerate(temporaryC) if x == 2]
    for i in range(len(c2list)):
        Answer2 += temporaryP[c2list[i]]
    print(Answer1, Answer2)