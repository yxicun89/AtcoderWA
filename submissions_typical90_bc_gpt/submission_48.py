N, P, Q = map(int, input().split())

A = list(map(int, input().split()))

count = 0

for i in range(N):
  for j in range(i+1,N):
    for h in range(j+1, N):
      for k in range(h+1, N):
        for m in range(k+1, N):
          #print(i, j, h, k, m)
          #print(i*j*h*k*m)
          if (i*j*h*k*m)%P==Q:
            count+=1

print(count)