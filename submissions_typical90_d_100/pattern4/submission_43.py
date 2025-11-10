# リスト初期化エラー

H, W = map(int, input().split())

A = [[0]*W]*H

A_tate = [0]*W

A_yoko = [0]*H

B = [[0]*W]*H

for i in range(H):

    A[i] = list(map(int, input().split()))

    A_yoko[i] = sum(A[i])



for i in range(W):

  for j in range(H):

    A_tate[i] += A[j][i]



for i in range(W):

  for j in range(H):

    B[j][i] = A_tate[i]+A_yoko[j]-A[j][i]



for i in range(H):

    print(' '.join(map(lambda j: str(B[i][j]), range(W))))
