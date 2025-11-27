H, W = map(int, input().split())

if H == 1 and W == 2 :

  print(2)

  exit()

if H == 2 and W == 1 :

  print(2)

  exit()



print(((H + 1) // 2) * ((W + 1) // 2))
