N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
k = sum(abs(A[i]-B[i]) for i in range(N))
print("Yes" if (K-k) % 2 == 0 else "No")