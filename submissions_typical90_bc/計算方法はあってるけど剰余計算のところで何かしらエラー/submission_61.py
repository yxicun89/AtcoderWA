N,P,Q=map(int,input().split())
A=list(map(int,input().split()))
cnt=0
for a in range(N):
  for b in range(a):
    for c in range(b):
      for d in range(c):
        for e in range(d):
          if (a*b*c*d*e)%P==Q:
            cnt+=1
print(cnt)