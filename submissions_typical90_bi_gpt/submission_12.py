# カードの操作を行うプログラム



def card_operations(operations):

    stack = []  # 山札を表すスタック

    output = []  # 出力結果を格納するリスト



    for op in operations:

        t, x = op

        if t == 1:

            stack.append(x)  # 上にカードを追加

        elif t == 2:

            stack.insert(0, x)  # 下にカードを追加

        elif t == 3:

            output.append(stack[x - 1])  # 上からx番目のカードを出力



    return output



# 入力を受け取る

Q = int(input())

operations = [tuple(map(int, input().split())) for _ in range(Q)]



# 操作を実行し、結果を得る

results = card_operations(operations)



# 結果を出力

for result in results:

    print(result)

