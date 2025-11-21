N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
  exit(print("No"))

cnt = 0
for i in range(N):
  cnt += abs(A[i] - B[i])

print("Yes" if cnt <= K else "No")