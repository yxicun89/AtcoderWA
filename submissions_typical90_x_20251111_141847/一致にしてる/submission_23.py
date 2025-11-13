# 以下じゃなくて一致
N,K = map(int,input().split())

An = list(map(int,input().split()))

Bn = list(map(int,input().split()))

cnt= 0



for i in range(N):

  if An[i] == Bn[i]:

    continue

  else:

    cnt += abs(An[i]-Bn[i])



if cnt == K or (K-cnt)%2==0:

  print('Yes')

else:

  print('No')

