N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print("Yes" if sum(abs(a - b) for a, b in zip(A, B)) and (sum(A) - sum(B) + K) % 2 == 0 else "No")