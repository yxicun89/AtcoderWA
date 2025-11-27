N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

gap = [a-b for a, b in zip(A, B)]

sum_abs=0
for i in gap:
    sum_abs += abs(i)


if (sum_abs - K) % 2 == 0:
    print("Yes")
else:
    print("No")
