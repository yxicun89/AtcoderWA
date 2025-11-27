H,W=map(int,input().split())
ans=(H//2)*(W//2)

if H%2+W%2==1:
    if H%2==0:
        ans+=H//2
    else:
        ans+=W//2

elif H%2+W%2==2:
    ans+=H//2+W//2+1

print(ans)
