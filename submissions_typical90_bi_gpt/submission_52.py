
q = int(input())

x_list = []

for i in range(q):

  t, x = map(int, input().split())

  if t == 1:

    x = x / 100000

    x_list = x_list + [x]

  elif t == 2:

    x = x / 100000

    x_list = [x] + x_list

  else:

    print(int(x_list[-x] * 100000))
