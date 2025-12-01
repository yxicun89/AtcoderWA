def count_evens(numbers):
    count = 0              # ① 開始・初期化 (Block)

    for n in numbers:      # ② ループ条件 (Decision / 菱形)
                           #    (リストにまだ要素があるか？)

        if n % 2 == 0:     # ③ 分岐条件 (Decision / 菱形)
                           #    (偶数か？)

            count += 1     # ④ 処理 (Block / 長方形)

    return count           # ⑤ 終了 (Block)
