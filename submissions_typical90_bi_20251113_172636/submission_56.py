Q=int(input())
P=[]
for i in range(Q):
    t,x=map(int,input().split())
    P.append((t,x))

A=''
ans=[]
for i in P:
    if i[0]==1:
        A= str(i[1])+ A
    elif i[0]==2:
    	A = A + str(i[1])
    else:
        ans.append(A[i[1]-1])

print(*ans,sep='\n')