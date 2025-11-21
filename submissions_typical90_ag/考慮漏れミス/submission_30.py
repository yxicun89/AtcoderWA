
# input
H, W = map(int, input().split())

# logic
if H >= 2 and W >= 2:
    print(((H + 1) // 2) * ((W + 1) // 2))
elif H == 1 or W == 1:
    print(0)
