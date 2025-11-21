a,b,c=map(int,input().split())
a,b,c=sorted([a,b,c])
s=a+b+c
while min(b%a,c%a)!=0:
  a,b,c=b%a,c%a,a
  if a>b:b,a=a,b
print(s//a-3)