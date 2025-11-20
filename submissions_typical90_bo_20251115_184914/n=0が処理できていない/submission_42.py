hati = [1]*21
for i in range(1,21):
    hati[i] = hati[i-1]*8
def eton(X):
    t = 0
    for i in range(len(X)-1,-1,-1):
        t += int(X[i])*hati[len(X)-i-1]
    S = ""
    while t>0:
        if t%9==8:tmp=5
        else:tmp = t%9
        S = str(tmp)+S
        t//=9
    return S
N,K = map(int,input().split())
ans = str(N)
for i in range(K):
    ans = eton(ans)
print(ans)