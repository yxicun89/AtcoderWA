n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for a, b in zip(A, B):
    res += abs(a - b)

if (k - res) % 2 == 0:
    print("Yes")
else:
    print("No")
