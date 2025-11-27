N=int(input())
CP=[]
for i in range(N):
  CP.append(list(map(int,input().split(" "))))
Q=int(input())
Ans={}
LR=[]
for q in range(Q):
  LR.append(tuple(map(int,input().split(" "))))

small=99999
big=0
for lr in LR:
  Ans[lr]=[0,0]
  small=min(small,lr[0])
  big=max(big,lr[1])
tLR=list(LR)
for i in range(small-1,big):
  for lr in tLR:
    if lr[0]-1<=i and i<lr[1]:
      if CP[i][0]==1:
        Ans[lr][0]+=CP[i][1]
      else:
        Ans[lr][1]+=CP[i][1]
for lr in LR:
  print(Ans[lr][0],Ans[lr][1])