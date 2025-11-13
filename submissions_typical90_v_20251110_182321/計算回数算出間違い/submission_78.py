
def gcd(a,b):

    saki= a
    ato = b

    temp =-1
    while temp !=0:
            temp = saki % ato
            if temp == 0:
                return ato
            else:
                saki = ato
                ato = temp
    

a,b,c = map(int,input().split())

gcd_num = gcd(gcd(a,b),c)

print((a+b+c-3)//gcd_num)