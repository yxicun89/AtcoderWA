H, W = map(int, input().split())

if H == 1 or W == 1:
  print(H * W // 2)
elif H % 2 == 0:
  if W % 2 == 0:
    print((H // 2) * (W // 2))
  else:
    print((H // 2) * ((W + 1) // 2))
else:
  if W % 2 == 0:
    print(((H + 1) // 2) * (W // 2))
  else:
    print(((H + 1) // 2) * ((W + 1) // 2))