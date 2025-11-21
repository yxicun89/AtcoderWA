N, P, Q = map(int,input().split())
A = list(map(int,input().split()))

count = 0
for a in range(N-4):
  for b in range(a+1, N-3):
    for c in range(b+1, N-2):
      for d in range(c+1, N-1):
        for e in range(d+1, N):
          if (a*b*c*d*e % P == Q):
            count +=1
print(count)