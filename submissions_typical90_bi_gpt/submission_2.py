

from collections import deque



Q = int(input())

deck = deque()

cnt = [0] * (Q + 1)

task = []



for i in range(1, Q + 1):

    cnt[i] += cnt[i - 1]

    t, x = map(int, input().split())

    if t == 1:

        deck.appendleft(x)

        cnt[i] += 1

    elif t == 2:

        deck.append(x)

    elif t == 3:

        task.append((i, x))



for i, x in task:

    ue = cnt[Q] - cnt[i]

    print(deck[x - ue - 1])
