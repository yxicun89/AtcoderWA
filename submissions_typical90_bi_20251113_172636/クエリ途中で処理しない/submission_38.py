# 山札の状態をクエリごとに管理できていない

Q = int(input())



T = []

X = []

cnt_1 = 0

cnt_2 = 0



for i in range(Q):

    t, x = map(int, input().split())

    if t == 1:

        cnt_1 += 1

    if t == 2:

        cnt_2 += 1

    T.append(t)

    X.append(x)



li = [0]*(cnt_1 + cnt_2)



for i in range(Q):

    if T[i] == 1:

        li[cnt_1-1] = X[i]

        cnt_1 -= 1

    if T[i] == 2:

        li[-cnt_2] = X[i]

        cnt_2 -= 1

    if T[i] == 3:

        print(li[X[i]-1])
