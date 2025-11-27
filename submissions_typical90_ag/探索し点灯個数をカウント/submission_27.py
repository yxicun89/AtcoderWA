
H,W=list(map(int,input().split()))
S=[["."]*W for _ in range(H)]
ans=0
for i in range(H):
    for j in range(W):
        cnt=0
        for ii in range(-1,2):
            for jj in range(-1,2):
                if 0<=i+ii<H and 0<=j+jj<W and S[i+ii][j+jj]=="#":
                    cnt+=1
        if not cnt:
            S[i][j]="#"
            ans+=1
print(ans)