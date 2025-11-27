n,k=input().split();n=[*map(int,n)]

for i in[0]*int(k):

 for j in n:i=8*i+j

 r=[]

 while i:r+=i%9,;i//=9

 n=[j-3*(j==8)for j in r[::-1]]

print(*n,sep='')
