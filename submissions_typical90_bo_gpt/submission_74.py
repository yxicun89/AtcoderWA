N,K=input().split()

now=N
for k in range(int(K)):
    x10=0
    f=1
    for i in range(1,len(now)+1):
       x10+=int(now[-1*i])*f
       f*=8
    temp=""
    while x10!=0:
        if x10%9==8:
            temp="5"+temp
        else:
            temp=str(x10%9)+temp
        x10=x10//9
    now=temp

print(now)

