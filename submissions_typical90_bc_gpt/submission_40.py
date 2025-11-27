
N, P, Q = map(int, input().split())

A = list(map(int, input().split()))



cnt = 0

for a in range(N-4):

  for b in range(a+1, N-3):

    x = (A[a]*A[b]) % P

    for c in range(b+1, N-2):

      x = (x*A[c]) % P

      for d in range(c+1, N-1):

        x = (x*A[d]) % P

        for e in range(d+1, N):

          x = (x*A[e]) % P

          if x == Q:

            cnt += 1

print(cnt)

