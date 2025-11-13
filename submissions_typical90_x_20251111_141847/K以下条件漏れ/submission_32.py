N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
check = []
for i in range(N):
    if A[i] != B[i]:
        check.append(abs(A[i] - B[i]))
print("Yes" if (sum(check) - K) % 2 == 0 else "No")
