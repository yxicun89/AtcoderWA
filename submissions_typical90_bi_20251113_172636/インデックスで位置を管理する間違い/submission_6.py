# 値代入してるから上書きされる

q=int(input())

cards={}

R=0

L=0

A=0

for i in range(q):

    t,x=map(int,input().split())

    if A==0:

        cards[0]=x

        A=1



    if t==1:

        R+=1

        cards[R]=x

    if t==2:

        L-=1

        cards[L]=x

    if t==3:

        print(cards[R-x+1])
