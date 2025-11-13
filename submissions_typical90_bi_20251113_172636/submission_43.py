from collections import deque

q = int(input())
tx = [list(map(int, input().split())) for i in range(q)]

deq = deque()
for i in tx:
    if i[0] == 1:
        deq.appendleft(i[1])
    if i[0] == 2:
        deq.append(i[1])

lst = list(deq)
for i in tx:
    if i[0] == 3:
        print(lst[i[1]-1])