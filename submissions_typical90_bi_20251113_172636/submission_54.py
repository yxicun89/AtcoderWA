# KYO061
from collections import deque
from itertools import islice
import heapq

Q = int(input())
que = deque()
LQ =[]
for i in range(Q):
    inputs = list(map(int, input().split()))
    if inputs[0] == 1:
        que.append(inputs[1])
    elif inputs[0] == 2:
        que.append(inputs[1])
    elif inputs[0] == 3:
        LQ = list(que)
        print(LQ[inputs[1]-1])
        LQ.clear()