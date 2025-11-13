# input
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# logic
r = abs(sum(A)-sum(B))

if K - r >= 0 and (K - r) % 2 == 0:
    print("Yes")
else:
    print("No")
