import collections

Q=int(input())

queue = collections.deque()
for q in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        # キューの右に追加
        queue.append(x)
    elif t == 2:
        # キューの左に追加
        queue.appendleft(x)
    else:
        # x番目の要素を書きだす
        print(queue[x-1])
