N=int(input())
C=[]
P=[]

for i in range(N):
    c,p=map(int,input().split())
    C.append(c)
    P.append(p)

p1=0
p2=0
P1=[0]
P2=[0]

for i in range(N):
    if C[i]==1:
        p1+=P[i]
    else:
        p2+=P[i]
    P1.append(p1)
    P2.append(p2)

Q=int(input())
for i in range(Q):
    l,r=map(int,input().split())
    print(f"{P1[r]-P1[l-1]}{P2[r]-P2[l-1]}")
