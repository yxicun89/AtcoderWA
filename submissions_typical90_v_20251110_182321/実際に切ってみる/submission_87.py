A, B, C = map(int, input().split())
min_cut = 0
if A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    vlen = min([A,B,C])
    while vlen > 1:
        if A % vlen == 0 and B % vlen == 0 and C % vlen == 0:
            min_cut = A // vlen + B // vlen + C // vlen - 3
            break
        vlen -= 2
else:
    min_cut = A + B + C - 3

print(min_cut)
