#累積和しようしていない

N = int(input())

A, B = [], []

for _ in range(N):
    x, val = map(int, input().split())   # ← 修正：input().split()
    if x == 1:
        A.append(val)
    else:
        B.append(val)

Q = int(input())
L = [list(map(int, input().split())) for _ in range(Q)]

X = []
for i, j in L:
    A_sum = sum(A[i:j+1])
    B_sum = sum(B[i:j+1])
    X.append([A_sum, B_sum])

for a_sum, b_sum in X:
    print(a_sum, b_sum)
