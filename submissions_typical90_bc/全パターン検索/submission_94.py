from functools import lru_cache

# 入力を受け取る
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

count = 0

# 再帰とメモ化で組み合わせを探索する
@lru_cache(None)
def dfs(depth, index, product):
    global count
    if depth == 5:
        if product == Q:
            count += 1
        return
    
    for i in range(index, N):
        # 次の積を計算してPで割った余りのみを保持
        dfs(depth + 1, i + 1, (product * A[i]) % P)

# 深さ0からスタートし、再帰的に5つの要素を選ぶ
dfs(0, 0, 1)

# 結果を出力
print(count)
