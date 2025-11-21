n,p,q=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for i in range(n-4):
  for j in range(i+1,n-3):
    for k in range(j+1,n-2):
      for y in range(k+1,n-1):
        for t in range(y+1,n):
          if i*j*k*y*t%p==q:
            cnt+=1
print(cnt)