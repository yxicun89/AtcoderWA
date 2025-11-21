A, B, C = map(int, input().split())


def yukun(x, y):  # X＞Y
    by, M = 1, 1
    while by != 0:
        by = x % y
        x = y
        y = by
    return x


if A > B:
    ab = yukun(A, B)
elif A < B:
    ab = yukun(B, A)
else:
    ab = A

if C > ab:
    abc = yukun(C, ab)
elif C < ab:
    abc = yukun(ab, C)
else:
    abc = ab

sum = -3 + (A/abc) + (B/abc) + (C/abc)
print(int(sum))