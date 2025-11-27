N=int(input())



S={}

for n in range(1,N):

  U=input()

  if U in S:

    continue

  print(n)

  S[U]=0
