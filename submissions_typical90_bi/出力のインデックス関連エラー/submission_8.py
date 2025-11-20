# t=2がappendじゃなくてinsertになっていた

Q = int(input())

A = [list(map(int, input().split())) for _ in range(Q)]



D = []

for t, x in A:

  if t==1:

    D.insert(0,x)

  if t==2:

    D.insert(-1,x)

  if t==3:

    print(D[x-1])
