data = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [a - b for a, b in zip(A, B)]
diff_abs = list(map(abs, diff))

if sum(diff_abs)%2 == data[1]%2:
  print("Yes")
elif sum(diff_abs)%2 != data[1]%2:
  print("No")