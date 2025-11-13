N=int(input())

sum_C1=0
sum_C2=0
C1=[]
C2=[]

for i in range(N):
    C,P=map(int,input().split())
    if C==1:
        sum_C1+=P
    else:
        sum_C2+=P
    C1.append(sum_C1)
    C2.append(sum_C2)

Q=int(input())

for i in range(Q):
    L,R=map(int,input().split())
    print(C1[R-1]-C1[L-2],C2[R-1]-C2[L-2])