h,w=map(int,input().split())
if h%2==0:
    x=h//2
else:
    x=h//2+1
if w%2==0:
    y=w//2
else:
    y=w//2+1
print(x*y)