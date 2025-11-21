# ライブラリ使わない浮動小数エラー

A = list(map(int, input().split( )))

a = sum(A) - 3

b = 0

B, S = A[2], A[1]

while B % S != 0:

    T = B % S

    B = S

    S = T

if A[0] % S == 0 and A[2] != A[0]:

    b += (A[0] - A[0]/S) + (A[1] - A[1]/S) + (A[2] - A[2]/S)

    A[0], A[1], A[2] = A[0]/S, A[1]/S, A[2]/S

B, S = A[2], A[0]

while B % S != 0:

    T = B % S

    B = S

    S = T

if A[1] % S == 0 and A[2] != A[0]:

    b += (A[0] - A[0]/S) + (A[1] - A[1]/S) + (A[2] - A[2]/S)

    A[0], A[1], A[2] = A[0]/S, A[1]/S, A[2]/S

B, S = A[1], A[0]

while B % S != 0:

    T = B % S

    B = S

    S = T

if A[2] % S == 0 and A[2] != A[0]:

    b += (A[0] - A[0]/S) + (A[1] - A[1]/S) + (A[2] - A[2]/S)

    A[0], A[1], A[2] = A[0]/S, A[1]/S, A[2]/S

print(int(a - b))

