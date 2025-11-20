Q=int(input())
q=[]
for i in range(Q):
    t,x=map(int,input().split())
    if t == 1:
        q.append(x)
    elif t == 2:
        q.insert(0,x)
    else:
        print(q[x-1])