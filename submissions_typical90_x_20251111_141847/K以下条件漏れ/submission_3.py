import sys
input = sys.stdin.readline


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_diff = 0
for i in range(N):
  total_diff += abs(A[i] - B[i])

print('Yes' if abs(K - total_diff) % 2 == 0 else 'No')