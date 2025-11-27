
H, W = map(int, input().split())

if (H or W ) == 1:

    print(H+W-1)

else:

    print(((H+1)//2)*((W+1)//2))
