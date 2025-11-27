N=int(input())

data1,data2=[0]*N,[0]*N
for i in range(N):
  C,P = map(int,input().split())
  if C==1:
    data1[i]=P
  else:
    data2[i]=P

sum_1,sum_2 = [0]*(N+1),[0]*(N+1)

for i in range(1,N+1):
  sum_1[i]=sum_1[i-1]+data1[i-1]
  sum_2[i]=sum_2[i-1]+data2[i-1]

Q = int(input())


for i in range(Q):
  L,R  = map(int,input().split())
  print(sum_1[R]-sum_1[L],sum_2[R]-sum_2[L])
