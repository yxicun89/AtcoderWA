a,b,c = list(map(int, input().split()))

def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a > b:
            return gcd(b,a%b)
        else:
            return gcd(a,b%a)
         
            
GCD = gcd(a,gcd(b,c))
result = int((a+b+c-3)/GCD )
print(result)