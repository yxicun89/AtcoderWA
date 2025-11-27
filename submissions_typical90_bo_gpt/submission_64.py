n,k=map(int,input().split())
n=str(n)
for i in range(k):
    A=""
    p=0
    for j in range(len(n)):
        p+=int(n[len(n)-j-1])*8**j
    while p!=0:
        if p%9==8:A+=str(5)
        else:A+=str(p%9)
        p=p//9
    n=A[::-1]
print(n)