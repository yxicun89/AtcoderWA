#セッション情報入れればatcoderから1ページ分の提出一覧データを取得できる
#ユーザー名取得して30個のコードというより30人のコードにしたい

import time
import random
import os
import datetime
import re

import requests
from bs4 import BeautifulSoup

def count_print_statements(source_code):
    """
    ソースコードのprint文の数をカウントする関数

    Args:
        source_code (str): Pythonのソースコード

    Returns:
        int: print文の数
    """
    # print文のパターンを定義（コメントアウトされたものは除外）
    # print(...)やprint ...の形式をカウント
    pattern = r'^\s*print\s*\('

    lines = source_code.split('\n')
    print_count = 0

    for line in lines:
        # コメントアウトされた行は除外
        stripped_line = line.strip()
        if stripped_line.startswith('#'):
            continue

        # 行の中でコメント部分を除去
        if '#' in line:
            code_part = line.split('#')[0]
        else:
            code_part = line

        # print文をカウント
        if re.search(pattern, code_part):
            print_count += 1

    return print_count

def scrape_atcoder_submissions(session_key, task_id="d", target_count=30, contest="typical90", max_pages=10):
    """
    AtCoderの提出一覧からユニークなユーザーのソースコードを取得する関数

    Args:
        session_key (str): REVEL_SESSION のキー
        task_id (str): タスクID (例: "d" for typical90_d)
        target_count (int): 取得したいユニークユーザー数
        contest (str): コンテスト名 (例: "typical90")
        max_pages (int): 最大検索ページ数（安全装置）

    Returns:
        dict: 処理結果の統計情報
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Cookie': f'REVEL_SESSION={session_key}',
    }

    # ベースURL生成
    base_url = f"https://atcoder.jp/contests/{contest}/submissions?f.Task={contest}_{task_id}&f.LanguageName=Python&f.Status=WA&f.User="

    sleep_time = random.uniform(2, 5)  # 2〜5秒の間でランダム待機

    # submissionsディレクトリ名にタイムスタンプを追加
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_dir = f"submissions_{contest}_{task_id}_{current_time}"
    os.makedirs(unique_dir, exist_ok=True)

    # 既に処理したユーザー名を記録するセット
    processed_users = set()
    submission_count = 0  # 実際に保存した提出数をカウント
    skipped_by_print = 0  # print文が多すぎてスキップした数

    print(f"=== {contest}_{task_id} の提出を取得開始 ===")
    print(f"目標取得数: {target_count} 人")
    print(f"最大検索ページ数: {max_pages}")
    print(f"保存先ディレクトリ: {unique_dir}")
    print(f"フィルタ条件: print文が2つ未満のコードのみ保存")

    # 複数ページを処理
    for page in range(1, max_pages + 1):
        print(f"\n--- ページ {page} を処理中 ---")
        print(f"現在の取得数: {submission_count}/{target_count}")

        # 目標数に達した場合は終了
        if submission_count >= target_count:
            print(f"目標取得数 {target_count} に達しました。処理を終了します。")
            break

        # ページURLを生成
        if page == 1:
            page_url = base_url
        else:
            page_url = f"{base_url}&page={page}"

        print(f"URL: {page_url}")

        # ページを取得
        response = requests.get(page_url, headers=headers)
        html = response.text

        # BeautifulSoupでHTMLをパース
        soup = BeautifulSoup(html, "html.parser")

        # テーブル本体のtbodyを取得
        tbody_selector = "#main-container > div.row > div:nth-child(3) > div > div.table-responsive > table > tbody"
        tbody = soup.select_one(tbody_selector)

        if tbody:
            rows = tbody.find_all("tr")
            print(f"ページ {page} のデータ数: {len(rows)}")

            if len(rows) == 0:
                print(f"ページ {page} にデータがありません。処理を終了します。")
                break

            for i, row in enumerate(rows, 1):
                # ユーザー名を取得（3列目のaタグ）
                user_tag = row.select_one("td:nth-child(3) > a:nth-child(1)")
                if user_tag:
                    username = user_tag.get_text().strip()

                    # 既に処理済みのユーザーはスキップ
                    if username in processed_users:
                        print(f"ページ{page}-{i}: ユーザー {username} は既に処理済みのためスキップ")
                        continue

                    # ユーザーを処理済みリストに追加
                    processed_users.add(username)
                    print(f"ページ{page}-{i}: ユーザー {username} を処理中...")
                else:
                    print(f"ページ{page}-{i}: ユーザー名が見つかりませんでした")
                    continue

                # 各行の10列目のaタグ（解答URL）を取得
                a_tag = row.select_one("td:nth-child(10) > a")
                if a_tag:
                    relative_url = a_tag.get('href')
                    full_url = f"https://atcoder.jp{relative_url}"
                    print(f"ページ{page}-{i}: {full_url}")

                    time.sleep(sleep_time)
                    # 各URLにアクセスしてHTMLを取得しBeautifulSoupでパース
                    sub_response = requests.get(full_url, headers=headers)
                    sub_html = sub_response.text
                    sub_soup = BeautifulSoup(sub_html, "html.parser")

                    # pre要素からソースコードを取得
                    if sub_soup.pre and sub_soup.pre.string:
                        source_code = sub_soup.pre.string

                        # print文の数をカウント
                        print_count = count_print_statements(source_code)
                        print(f"ページ{page}-{i}: print文の数: {print_count}")

                        # print文が2つ以上ある場合はスキップ
                        if print_count >= 2:
                            print(f"ページ{page}-{i}: print文が{print_count}個あるためスキップ")
                            skipped_by_print += 1
                            continue

                        submission_count += 1
                        # 新しいPythonファイルとして保存（ユーザー名も含める）
                        filename = f"{unique_dir}/submission_{submission_count}.py"
                        with open(filename, "w", encoding="utf-8") as f:
                            f.write(source_code)
                        print(f"ソースコードを {filename} に保存しました")

                        # 目標数に達した場合は処理を終了
                        if submission_count >= target_count:
                            print(f"目標取得数 {target_count} に達しました。")
                            break
                    else:
                        print(f"ページ{page}-{i}: ソースコードが見つかりませんでした")

                    time.sleep(sleep_time)
                else:
                    print(f"ページ{page}-{i}: 解答URLが見つかりませんでした")

                # 目標数に達した場合は内側のループを抜ける
                if submission_count >= target_count:
                    break

            print(f"ページ {page} 処理完了")

            # 目標数に達した場合は外側のループも抜ける
            if submission_count >= target_count:
                break

            # ページ間の待機時間
            if page < max_pages:
                time.sleep(sleep_time)

        else:
            print(f"ページ {page} でテーブル本体が見つかりませんでした")
            break

    print(f"\n=== 全体処理完了 ===")
    if submission_count >= target_count:
        print(f"目標達成: {submission_count} 件のユニークなユーザーの提出を保存しました")
    else:
        print(f"処理完了: {submission_count} 件のユニークなユーザーの提出を保存しました（目標: {target_count}）")
    print(f"処理されたユーザー: {len(processed_users)} 人")
    print(f"print文フィルタでスキップ: {skipped_by_print} 件")
    print(f"処理したページ数: {page} ページ")

    # 結果を返す
    return {
        "submission_count": submission_count,
        "unique_users": len(processed_users),
        "pages_processed": page,
        "output_directory": unique_dir,
        "users_list": list(processed_users),
        "skipped_by_print": skipped_by_print
    }


# メイン実行部分
if __name__ == "__main__":
    # セッションキー（実際の値を入力してください）
    # session_key = input("REVEL_SESSION のキーを入力してください: ").strip() or ""
    # ユーザー入力でパラメータを指定
    task_id = input("タスクID を入力してください (例: d): ").strip() or "d"
    target_count = int(input("取得したいユーザー数を入力してください (例: 30): ").strip() or "30")
    contest = input("コンテスト名を入力してください (例: typical90): ").strip() or "typical90"

    # 関数を実行
    result = scrape_atcoder_submissions(
        session_key=session_key,
        task_id=task_id,
        target_count=target_count,
        contest=contest
    )

    print(f"\n=== 最終結果 ===")
    print(f"保存されたファイル数: {result['submission_count']}")
    print(f"ユニークユーザー数: {result['unique_users']}")
    print(f"print文フィルタでスキップ: {result['skipped_by_print']} 件")
    print(f"処理ページ数: {result['pages_processed']}")
    print(f"出力ディレクトリ: {result['output_directory']}")


# 問題番号対応表

# 4 cross sum d
# 2次元の表すべてでそのマスの縦横までの合計を求める
# ポイント：累積和を利用する、重複分の自身の値を引く

# 10 score j
# 累積和を2種類作る
# 学籍番号i,クラスCi,点数PiでLj~Rjの合計点数を求める
# ポイント：クラスごとに累積和を作成する
# sum1 = [0] * (N+1)  # クラス1の累積和
# sum2 = [0] * (N+1)  # クラス2の累積和

# 22 cubic v
# 幅A、高さB、奥行きCの直方体に対して最小何回ですべてのピースを立方体にできるのか
# 最大公約数 n = math.gcd(A, B, C)　切ったピースの辺がすべて共通の値かつでかい -> 最大公約数
# ans = A//n + B//n + C//n -3　過剰に数えた分を引く

# 24 select x
# 配列Aの各要素に対してちょうどK回 +1または-1を行えば配列Bと一致するか
# 各要素の差の絶対値の総和がK以下かつKと差の総和が偶数であれば可能(偶数は一致した後数合わせできるか)

# 27 sign aa
# ユーザーが何日目にログインしたか
# 重複したとき何もしないで初めて名前が出た時の日にちを表示する
# nが入力で受け付けてるから、for range(1,n+1)で回して確認すればok
# setでもdictでも

# 33 not ag
# イルミネーションがHW個のLEDで構成されている
# 2*2の領域で2つ以上点灯していたらアウト
# LEDの最大個数
# 片方が1だった場合は4領域作られないから全灯
# 奇数だったら余分に1個置けるからh+1/2個
# 偶数はh/2個
# wも同様でh*wが答え

# 55 select bc
# n個の整数から5個選んだ積をPで割るとQ余る組み合わせ
# 組み合わせをfor文で試す方法で行ける
# for i in range(N-4):
#     for j in range(i+1,N-3):
#         for k in range(j+1,N-2):
#             for l in range(k+1,N-1):
#                 for m in range(l+1,N):
#                     t=A[i]*A[j]%P*A[k]%P*A[l]%P*A[m]%P
#                     if t==Q:
#                         ans+=1

# 61 deck bi
# カード0枚から山札を作る
# Q個操作tiを行う
# ti=1:山札の一番上にカードを1枚追加
# ti=2:山札の一番上のカードを1枚追加
# ti=3:山札の上からxi番目のカードを書き出す
# ti=3printして出力して
# リスト使って先頭末尾でもいいしスタックキューでもOK(dequeなら両方合わせもってる)

# 67 base bo
# 8進数の整数Nに対して「Nを9進数にして8を5に置き換える」処理をK回行う
# 操作後の8進数を出力
# for _ in range(K):
#   n = int(N, 8)
#   res = ""
#   if n == 0:
#     res = "0"

#   while n > 0:
#     res = str(n % 9) + res
#     n //= 9
#   res = res.replace("8", "5")
#   N = res

# 78 easy bz
# n頂点M辺の単純無効グラフが与えられる
# aiとbiは双方向結んでる
# 自身より頂点番号が小さい隣接頂点がちょうど1個である頂点の数を求めよ

# 長さNの配列を用意し一つ一つの入力に対して大小関係を比較して増減を記録していく
# 配列の1の数が条件を満たすからそれを数えれば良い
