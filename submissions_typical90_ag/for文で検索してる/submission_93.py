h,w = map(int,input().split())

grid=["."*w for i in range(h)]
ans=0

if h<2 or w<2:
  print(1)
  exit()
for i in range(0,h,2):
  for j in range(0,w,2):
    ans+=1
print(ans)