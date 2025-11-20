n, k=input().split()
k=int(k)

for  i in range(k):
  value=0
  for j in range(len(n)):
    value+=8**j*int(n[-1-j])
  n=''
  while value>0:
    if value%9==8:
      n='5'+n
    else:
      n=str(value%9)+n
    value//=9
  
print(n)