
N = int(input())
A = [0] * (N+1)
B = [0] * (N+1)
for i in range(N):
    c,p = map(int, input().split())
    if c == 1:
        A[i] = p
    else:
        B[i] = p

for i in range(N):
    A[i+1] += A[i]
    B[i+1] += B[i]

for _ in range(int(input())):
    L,R = map(int, input().split())
    print(A[R] - A[L-1], B[R] - B[L-1])
