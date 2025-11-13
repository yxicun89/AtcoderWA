# 重複していた時printしている

n = int(input())

ss = []

for i in range(n):

  s = input()

  if not s in ss:

    ss.append(s)

  else:

    print(i + 1)
