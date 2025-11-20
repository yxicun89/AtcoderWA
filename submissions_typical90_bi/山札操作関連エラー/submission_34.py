# 山札の状態管理エラー

q=int(input())

a1=[]

a2=[]

a3=[]

for i in range(q):

    t,x=map(int,input().split())

    if t==1:

        a1.append(x)

    elif t==2:

        a2.append(x)

    else:

        a3.append(x)

a1.reverse()

a=a1+a2

for i in a3:

    print(a[i-1])
