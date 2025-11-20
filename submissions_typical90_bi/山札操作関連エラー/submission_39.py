# 文字列管理でエラー

n = int(input())

order_list = [tuple(map(int, input().split())) for _ in range(n)]

deck_set = ''



for i in range(n):

  order = order_list[i]

  action, number = order[0], order[1]

  if action == 1:

    deck_set = str(number) + deck_set

  elif action == 2:

    deck_set = deck_set + str(number)

  else:

    print(deck_set[number-1])
