
H,W = map(int,input().split())



A = []

for h in range(H):

  B = list(map(int,input().split()))

  A.append(B)



hsum = []

for h in range(H):

  count = 0

  for w in range(W):

    count += A[h][w]

  hsum.append(count)



wsum = []

for w in range(W):

  count = 0

  for h in range(H):

    count += A[h][w]

  wsum.append(count)



for h in range(H):

  for w in range(W-1):

    print(wsum[w] + hsum[h]-A[h][w],end = " ")

  print(wsum[W-1]+hsum[h]-A[h][w],end = "\n")
