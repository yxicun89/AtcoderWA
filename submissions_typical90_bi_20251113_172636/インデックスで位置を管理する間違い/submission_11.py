# インデックス管理エラー

n=int(input())

D=[0]*(2*n)

start=n

goal=n

for i in range(n):

    a,b=map(int,input().split())

    if a==1:

        D[start]=b

        start-=1

    if a==2:

        D[goal]=b

        goal+=1

    if a==3:

        print(D[start+b])
