
q=int(input())

yl=[]#山札のリスト

for i in range(q):

  t,x=map(int,input().split())

  if(t==1):

    yl.append(x)

  elif(t==2):

    yl.insert(0,x)

  elif(t==3):

    print(yl[x-1])

