N, K = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

count = 0

for n in range(N):
  while (A_list[n] != B_list[n]) or (count != K):
    if A_list[n] == B_list[n]:
      break
    elif A_list[n] < B_list[n]:
      A_list[n] += 1
    else:
      A_list[n] -= 1
    count += 1

# 途中終了偶数の可能性があり
if (A_list != B_list) or (K - count) % 2 != 0:
  print('No')
elif (K - count) % 2 == 0:
  print('Yes')