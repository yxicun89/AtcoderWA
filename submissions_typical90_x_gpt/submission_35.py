# input
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# calculate
# dp?
c = [b[i]-a[i] for i in range(n)]

def count_up(num_list):
  count = 0
  for num in num_list:
    if num >= 0:
      count += num
    else:
      count -= num
  return count

print(k - count_up(c))
if (k - count_up(c))%2 == 0:
  print("Yes")
else:
  print("No")