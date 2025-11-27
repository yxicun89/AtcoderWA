H,W = map(int,input().split())

if H % 2 == 1:
    H += 1
if W % 2 == 1:
    W += 1
    
print((W//2) * (H//2))

