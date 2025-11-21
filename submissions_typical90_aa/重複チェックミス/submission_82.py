# 重複したときにインデックスを出力しない

N = int(input())

U = []

P = set()

for i in range(N):

    S = input()

    U.append(S)

    P.add(U.index(S))

U = list(P)

U.sort

M = len(U)

for j in range(M):

    print(U[j]+1)
