N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sum = sum(A)
B_sum = sum(B)

if (abs((A_sum - B_sum)) + K) % 2 == 0:
  print("Yes")
else:
  print("No")