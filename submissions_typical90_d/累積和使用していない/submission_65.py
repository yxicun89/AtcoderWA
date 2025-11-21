

def LI(): return list(map(int, input().split()))

H,W = LI()

A = [LI() for i in range(H)]

B = [[0 for i in range(W)] for j in range(H)]

for i in range(H):

    for j in range(W):

        for x in range(H):

            B[i][j] += A[x][j]

        for y in range(W):

            B[i][j] += A[i][y]

        B[i][j] -= A[i][j]

for i in range(H):

    print(B[i])
