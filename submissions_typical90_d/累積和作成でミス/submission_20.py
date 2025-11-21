# 初期化でリストをコピーしてしまうと、参照渡しになるため注意

h, w = map(int, input().split())

S = [list(map(int, input().split())) for _ in range(h)]

row = list(map(sum, S))

col = list(map(sum, zip(*S)))

ans = [[0] * w] * h

for i in range(h):

    for j in range(w):

        ans[i][j] = row[i] + col[j] - S[i][j]



for str in ans:

    print(*str)
