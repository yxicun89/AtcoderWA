from collections import defaultdict
n,m=map(int,input().split())
aaa=defaultdict(set)
for i in range(m):
    a,b=map(int,input().split())
    aaa[a].add(b)
    aaa[b].add(a)
count=0
for i in range(1,n+1):
    z=list(aaa[i])
    try:
        if z[0]<i and z[1]>i:
            count+=1
    except IndexError:
        if z[0]<i:
            count+=1
print(count)