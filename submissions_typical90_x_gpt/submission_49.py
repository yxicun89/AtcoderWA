N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

abss = [abs(A[i] - B[i]) for i in range(N)]

print("Yes" if (sum(abss) % 2) == K % 2 else "No")