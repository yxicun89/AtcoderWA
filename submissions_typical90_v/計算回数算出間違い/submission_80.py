def aa(x,y):
  while True:
    if x>y:
      x,y=y,x
    if y%x==0:
      return x
    x,y=y-x,x
  

a,b,c=map(int,input().split())
v=aa(a,aa(b,c))
print(a//v+b//v+c//v)