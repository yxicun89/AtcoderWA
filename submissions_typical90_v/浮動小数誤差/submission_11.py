# input
a, b, c = map(int, input().split())

# calculate
# GCD
def gcd(a, b):
    return gcd(b, a % b) if b else a

gcd_ab = gcd(a, b)
gcd_abc = gcd(gcd_ab, c)

ans = (a+b+c)/gcd_abc - 3

# output
print(ans)