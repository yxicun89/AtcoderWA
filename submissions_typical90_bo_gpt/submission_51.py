def Nto10(x,n):
    x = str(x)
    b10 = 0
    for i in range(len(x)):
        a = int(x[-1-i])
        b10 += n**i*a
    return b10

def Nfrom10(x,n):
    bn = 0
    x = str(x)
    for i in range(10*9):
        a,b = divmod(int(x),n)
        if a>n:
            bn += b*10**i
            x = a
        else:
            bn += b*10**i + a*10**(i+1)
            return bn

n,k = map(int,input().split())
for i in range(k):
    n = Nto10(n,8)
    # print(n)
    n = Nfrom10(n,9)
    # print(n)
    n = int(str(n).replace("8","5"))
    # print(i+1,n)
    
print(n)
