# 隣接条件が距離で不適切

N, M = map(int, input().split())



a = []

b = []



for i in range(M):

    x,y = map(int,input().split())

    a.append(x)

    b.append(y)



count = 0



for i in range(1,M):

    dist = 0

    num = 0

    for j in range(i):

        dist += abs(a[i]-a[j]) + abs(b[i]-b[j])

        if dist == 1:

            num += 1



    if num == 1:

        count += 1



print(count)
