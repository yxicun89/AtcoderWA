
from collections import deque

q = int(input())



deck = deque()



for i in range(q):

    t, x = map(int,input().split())

    if t == 1:

        deck.append(x)

    if t == 2:

        deck.appendleft(x)

    if t == 3:

        print(deck[x-1])
