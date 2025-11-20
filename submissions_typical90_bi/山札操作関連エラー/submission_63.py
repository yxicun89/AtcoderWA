from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    q = int(input())
    TXs = [lmap(int, input().split()) for _ in range(q)]

    que = deque([])
    for t, x in TXs:
        if t == 1:
            que.append(x)
        elif t == 2:
            que.appendleft(x)
        else:
            print(que[x-1])


if __name__ == '__main__':
    main()
