# 入力
N = int(input())
student_info = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

# クラスごとの点数の合計を計算する
class_scores = [[0, 0] for _ in range(2)]
for student in student_info:
    class_idx, score = student
    class_scores[class_idx - 1][0] += score  # クラスごとの点数の合計を更新

# 累積和を計算する
cumulative_sum = [[0, 0] for _ in range(N + 1)]
for i in range(2):
    for j in range(1, N + 1):
        cumulative_sum[j][i] = cumulative_sum[j - 1][i] + class_scores[i][0]

# クエリーを処理し、結果を出力する
for query in queries:
    l, r = query
    class1_sum = cumulative_sum[r][0] - cumulative_sum[l - 1][0]
    class2_sum = cumulative_sum[r][1] - cumulative_sum[l - 1][1]
    print(class1_sum, class2_sum)