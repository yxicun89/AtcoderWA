# 累積和はいいけど最後のprintが余分というか改行できるようにしたかったっぽい

H, W = list(map(int, input().split()))

A = [None]*H

for i in range(H):

    A[i] = list(map(int, input().split()))



sum_raw=[0]*H

for i in range(H):

  sum_raw[i]=0

  for j in range(W):

    sum_raw[i]+=A[i][j]



sum_column=[0]*W

for j in range(W):

  sum_column[j]=0

  for i in range(H):

    sum_column[j]+=A[i][j]



for i in range(H):

  for j in range(W-1):

    print(sum_raw[i] + sum_column[j] - A[i][j],end=" ")

  print(sum_raw[H-1] + sum_column[W-1] - A[H-1][W-1])
