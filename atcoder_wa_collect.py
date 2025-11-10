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
    session_key = "06722c346d933058258e302e378468655f148b05-%00csrf_token%3ATLIna2bZUW%2FL3Cd3OY40vyHyrJKO%2BuJTQJOoSZackGQ%3D%00%00SessionKey%3A0bf4c58671a33052101f582b64b660d346b9f89a30af2e1ec532db6371c83065%00%00UserScreenName%3Aeclips%00%00UserName%3Aeclips%00%00a%3Afalse%00%00w%3Afalse%00%00_TS%3A1778026944%00"
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
