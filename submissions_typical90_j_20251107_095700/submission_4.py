#クエリ計算時のインデックスエラー

from copy import deepcopy


n=int(input())

s=[[0]*2 for _ in range(n)]
for i in range(n):
    c,p=map(int,input().split())
    if i>0:
        s[i]=deepcopy(s[i-1])
    s[i][c-1]+=p

q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    res=[]
    for i in range(2):
        res.append(str(s[r-1][i]-s[l-2][i]))
    print(" ".join(res))
    








