S_list = []
N = int(input())
for i in range(N):
  S = input()
  if S in S_list:
    S_list.append(S)
    print(i + 1)

