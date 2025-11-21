H, W = map(int, input().split())
a = H // 2
b = W // 2

if H % 2 == 0 and W % 2 == 0 :
    count = a*b
    
elif H % 2 == 0 and W % 2 == 1 :
    count = a*(b+1)

elif H % 2 == 1 and W % 2 == 0 :
    count = (a+1)*b 

else:
    count = (a+1)*(b+1)-1

print(count)