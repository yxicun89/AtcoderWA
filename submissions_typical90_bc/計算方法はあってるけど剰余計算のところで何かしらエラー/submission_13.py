N,P,Q = map(int, input().split())
A = list(map(int, input().split()))
A = [i%P for i in A]

result = 0
for a in range(0,N-4):
  for b in range(a+1,N-3):
    for c in range(b+1,N-2):
      for d in range(c+1,N-1):
        for e in range(d+1,N):
          sum = a+b+c+d+e
          if(sum%P==Q):
            result = result + 1
print(result)
