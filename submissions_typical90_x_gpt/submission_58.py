N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

n = 0
for i in range(N):
    n += abs(A[i]-B[i])

if (K-n)%2 == 0:
    print("Yes")
else:
    print("No")