N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = sum(A[i] - B[i] for i in range(N))
print('Yes' if S <= K and S%2 == K%2 else 'No')