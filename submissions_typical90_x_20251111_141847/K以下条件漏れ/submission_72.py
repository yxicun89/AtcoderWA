inputs = lambda : map(int, input().split())

N, K = inputs()
A = list(inputs())
B = list(inputs())

cnt = 0
for i in range(N):
    a = A[i]
    b = B[i]

    if a < b:
        a, b = b, a

    c = a - b

    cnt += c

res = (K - cnt)%2
print('Yes' if res == 0 else 'No')