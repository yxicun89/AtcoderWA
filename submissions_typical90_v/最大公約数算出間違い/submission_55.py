a , b , c = map(int,input().split())

def gojohou(x,y):
    amari = x % y
    if amari == 0:
        return y
    else:
        gojohou(y,amari)
        return amari

ab = gojohou(max(a,b),min(a,b))
abc = gojohou(max(ab,c),min(ab,c))

print((a//abc-1) + (b//abc-1) + (c//abc-1))