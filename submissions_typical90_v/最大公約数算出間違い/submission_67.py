def gcd(a, b):
    r = a%b
    while r != 0:
        a, b = b, r
        r = a % b
    return b

A, B, C = map(int, input().split())
gcd_1 = gcd(A, B)
gcd_2 = gcd(B, C)
gcd_ans = min(gcd_1, gcd_2)

ans = (((A//gcd_ans)-1) + ((B//gcd_ans)-1) + ((C//gcd_ans)-1))
print(ans)