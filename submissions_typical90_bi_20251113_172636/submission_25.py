q=int(input())
tx=[list(map(int,input().split())) for _ in range(q)]
l=[]
ans=[]

for i in range(q):
    if tx[i][0]==1:
        l.insert(0,tx[i][1])
    elif tx[i][0]==2:
        l.append(tx[i][1])
    else:
        ans.append(l[tx[i][1]-1])
print(ans)