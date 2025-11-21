h,w=map(int,input().split())
if h==1 or w==1:
    print(0)
else:
    if h%2==0:
        hh=h//2
    else:
        hh=h//2+1

    if w%2==0:
        ww=w//2
    else:
        ww=w//2+1
    print(hh*ww)
