N = int(input())

S = set()

for i in range(N):

  A = set(input())

  if A <= S :

    pass

  else:

    S = S|A

    print(i+1)
