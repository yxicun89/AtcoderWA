H,W = map(int, input().split())

#2,3,4,5,6,
#1,2,2,3,3
ans = 0
if H >=2 and W >= 2:
    h = round(H/2)
    w = round(W/2)
    ans = h * w
else:
    ans = H*W
print(ans)
   