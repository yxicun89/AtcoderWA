# ヒープでエラー

#典型90問＿問題61



import heapq

q=int(input())

up=[]

down=[]

heapq.heapify(up)

heapq.heapify(down)

res=[]

u=0

d=0



for i in range(q):

    t,x=map(int,input().split())

    if t==1:

        heapq.heappush(up, x)

        u=u+1

    if t==2:

        heapq.heappush(down, x)

        d=d+1

    if t==3:

        if x<=u:

            res.append(up[x-1])

        else:

            res.append(down[d-(x-u)])



print(*res, sep="\n")



