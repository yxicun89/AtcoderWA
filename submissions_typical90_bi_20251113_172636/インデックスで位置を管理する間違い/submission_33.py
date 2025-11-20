# 山札上下をインデックスで管理するエラー
q = int(input())

deck = [0]*(2*q+1)

up = q

lo = q

for i in range(q):

    t,x = map(int, input().split())

    if t == 1:

        deck[up] = x

        up -= 1

    if t == 2:

        deck[lo] == x

        lo += 1

    if t == 3:

        print(deck[up+x-1])

