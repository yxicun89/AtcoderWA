A=list(map(int,input().split()))
def gojo2(a,b):
  if a>b:
    tmp=b
    b=a
    a=tmp
  while True:
    c=b//a
    d=b-a*c
    b=a
    a=d
    if d==0:
      break
  return b

def gojo3(a,b,c):
  d=gojo2(a,b);
  e=gojo2(a,c);
  return gojo2(d,e)

p=gojo3(A[0],A[1],A[2])
print(A[0]//p+A[1]//p+A[2]//p)