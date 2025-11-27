N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff_sum = sum(A) - sum(B)

print("Yes" if diff_sum%2 == K%2 else "No")