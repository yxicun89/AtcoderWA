A = list(map(int, input().split()))
def gcd(a, b):
    while b == 0:
        a, b = b, a % b
    return a 
gcd1 = gcd(A[0], A[1])
gcd2 = gcd(A[1], A[2])
gcd3 = gcd(gcd1, gcd2)

print(A[0] // gcd3 + A[1] // gcd3 + A[2] // gcd3 -3)