H,W = map(int,input().split())
if H % 2 == 0 and W % 2 == 0:
    print(H//2 * W // 2)
elif H % 2 == 1 and W % 2 == 1:
    print((H//2 + 1) * (W //2 + 1))
elif H % 2 ==1:
    print((H//2+1) * W//2)
elif W % 2 ==1:
    print(H//2 * (W//2 + 1))