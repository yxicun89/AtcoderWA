N=int(input())
a = [list(map(int, input().split())) for l in range(N)]
Q=int(input())
b = [list(map(int, input().split())) for l in range(Q)]
x=0
y=0
for i in range(Q):
    for j in range(b[i][0]-1,b[i][1]):
        if a[j][0]==1:
            x=x+a[j][1]
        else:
            y=y+a[j][1]
    print(x,y,end="\n")