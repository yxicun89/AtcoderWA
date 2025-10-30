# 重複分引いてない計算間違い

H,W=map(int,input().split())

A=[list(map(int,input().split())) for i in range(H)]

yoko=[]

tate=[]

for i in range(H):

    yoko.append(sum(A[i]))

for i in range(W):

    sums=0

    for j in range(H):

        sums+=A[j][i]

    tate.append(sums)



for i in range(H):

    for j in range(W):

        print(yoko[i]+tate[j],end=" ")

    print("")
