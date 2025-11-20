# インデックス管理ミス

Q = int(input())



deck = [-1 for _ in range(10**5)]

f = 0

l = 0



for _ in range(Q):

    t,x = map(int,input().split())

    if t == 1:

        if deck[f] != -1:

            f -= 1

        deck[f] = x

    elif t == 2:

        if deck[l] != -1:

            l -= 1

        deck[l] = x

    else:

        print(deck[f+x-1])

