from collections import deque

Q = int(input())  # クエリ数を取得
A = [tuple(map(int, input().split())) for _ in range(Q)]  # クエリをリストに格納

lst = deque()  # 高速なリスト操作のために deque を使用

for t, x in A:
    if t == 1:
        lst.append(x)  # 末尾に追加
    elif t == 2:
        lst.appendleft(x)  # 先頭に追加
    elif t == 3:
        index = x - 1  # 1-based index の可能性がある場合
        if 0 <= index < len(lst):  # インデックス範囲チェック
            print(lst[index])