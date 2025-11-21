A, B, C = map(int, input().split())
a = 1

while A % (2 * a) == 0 and B % (2 * a) == 0 and C % (2 * a) == 0:
    a *= 2

ans = A // a + B // a + C // a - 3
print(ans)
