from collections import deque
q=int(input())
a=[0 for i in range(1000000)]
t,x=map(int,input().split())
a[500000]=x
l=499999
r=500001
for i in range(q-1):
    t,x=map(int,input().split())
    if t==1:
        a[r]=x
        r+=1
    elif t==2:
        a[l]=x
        l-=1
    else:
        print(a[l+x])
