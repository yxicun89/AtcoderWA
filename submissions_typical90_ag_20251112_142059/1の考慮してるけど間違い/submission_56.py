h,w=map(int,input().split())
if h%2==1:
  h+=1
if w%2==1:
  w+=1
print(h*w//4)