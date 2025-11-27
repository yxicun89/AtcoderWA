
H,W=(int(x) for x in input().split())

b=[[0]*W for i in range(H)]



a=[list(map(int,input().split())) for _ in range(H)]



for i in range(H):

    for j in range(W):

        tmp=0

        for k in range(W):

            tmp+=a[i][k]

        for k in range(H):

            tmp+=a[k][j]

        b[i][j]=tmp

        print(b[i][j],end=" ")

    print()

