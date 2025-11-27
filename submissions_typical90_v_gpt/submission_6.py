
def gcd(x: int, y: int) -> int:

    while y:

        x, y = y, y % x

    return x





A, B, C = map(int, input().split())

r = gcd(A, gcd(B, C))

ans = (A // r + B // r + C // r) - 3

print(ans)
