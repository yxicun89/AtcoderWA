A, B, C = [int(i) for i in input().split()]

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

kouyaku = gcd(gcd(A, B), C)
# print(kouyaku)
ans = (A+B+C-3*kouyaku) / kouyaku
print(int(ans))