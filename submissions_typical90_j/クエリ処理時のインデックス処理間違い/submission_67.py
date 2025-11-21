N=int(input())
S=[]
for _ in range(N):
    S.append(input().split())
Q=int(input())
cs1=[0]*(N+1)
cs2=[0]*(N+1)
for i in range(N):
    if S[i][0]=='1':
        cs1[i+1]=cs1[i]+int(S[i][1])
        cs2[i+1]=cs2[i]
    else:
        cs1[i+1]=cs1[i]
        cs2[i+1]=cs2[i]+int(S[i][1])
        
for _ in range(Q):
    l,r =map(int,input().split())
    l-=1
    print(cs1[r]-cs1[1],cs2[r]-cs2[1])