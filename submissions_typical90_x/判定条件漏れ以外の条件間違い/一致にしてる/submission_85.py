n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0
def pm1(a, b, c):
    while a != b:
        if a < b:
            a += 1
            c += 1
        else:
            a -= 1
            c += 1
    return a, c
for i in range(n):
    A[i], count = pm1(A[i], B[i], count)
if count == k:
    print('Yes')
else:
    print('No')