n =int(input())

c1 =[0]*(n+1)
c2 =[0]*(n+1)
for _ in range(n):
    c,p = map(int,input().split())
    if c == 1:
        c1[_]=p
    else:c2[_]=p

a=0
b=0
for i in range(n):
    a+=c1[i]
    c1[i]=a

    b+=c2[i]
    c2[i]=b

q = int(input())

ans1=[]
ans2=[]
for i in range(q):
    l,r = map(int,input().split())
    ans1.append(c1[r]-c1[l-1])
    ans2.append(c2[r]-c2[l-1])

for _ in range(len(ans1)):
    print(abs(ans1[i]),abs(ans2[i]))