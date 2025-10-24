#セッション情報入れればatcoderから1ページ分の提出一覧データを取得できる
#ユーザー名取得して30個のコードというより30人のコードにしたい

import time
import random
import os
import datetime

import requests
from bs4 import BeautifulSoup

def scrape_atcoder_submissions(session_key, task_id="d", max_pages=3, contest="typical90"):
    """
    AtCoderの提出一覧からユニークなユーザーのソースコードを取得する関数
    
    Args:
        session_key (str): REVEL_SESSION のキー
        task_id (str): タスクID (例: "d" for typical90_d)
        max_pages (int): 取得する最大ページ数
        contest (str): コンテスト名 (例: "typical90")
    
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
    
    print(f"=== {contest}_{task_id} の提出を取得開始 ===")
    print(f"最大ページ数: {max_pages}")
    print(f"保存先ディレクトリ: {unique_dir}")
    
    # 複数ページを処理
    for page in range(1, max_pages + 1):
        print(f"\n--- ページ {page} を処理中 ---")
        
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
                        submission_count += 1
                        # 新しいPythonファイルとして保存（ユーザー名も含める）
                        filename = f"{unique_dir}/submission_{submission_count}_{username}.py"
                        with open(filename, "w", encoding="utf-8") as f:
                            f.write(source_code)
                        print(f"ソースコードを {filename} に保存しました")
                    else:
                        print(f"ページ{page}-{i}: ソースコードが見つかりませんでした")
                    
                    time.sleep(sleep_time)
                else:
                    print(f"ページ{page}-{i}: 解答URLが見つかりませんでした")
            
            print(f"ページ {page} 処理完了")
            
            # ページ間の待機時間
            if page < max_pages:
                time.sleep(sleep_time)
        
        else:
            print(f"ページ {page} でテーブル本体が見つかりませんでした")
            break

    print(f"\n=== 全体処理完了 ===")
    print(f"処理完了: {submission_count} 件のユニークなユーザーの提出を保存しました")
    print(f"処理されたユーザー: {len(processed_users)} 人")
    print(f"処理したページ数: {page} ページ")
    
    # 結果を返す
    return {
        "submission_count": submission_count,
        "unique_users": len(processed_users),
        "pages_processed": page,
        "output_directory": unique_dir,
        "users_list": list(processed_users)
    }


# メイン実行部分
if __name__ == "__main__":
    # セッションキー（実際の値を入力してください）
    session_key = input("REVEL_SESSION のキーを入力してください: ").strip() or ""
    # ユーザー入力でタスクIDを指定
    task_id = input("タスクID を入力してください (例: d): ").strip() or "d"
    max_pages = int(input("取得する最大ページ数を入力してください (例: 3): ").strip() or "3")
    contest = input("コンテスト名を入力してください (例: typical90): ").strip() or "typical90"
    
    # 関数を実行
    result = scrape_atcoder_submissions(
        session_key=session_key,
        task_id=task_id,
        max_pages=max_pages,
        contest=contest
    )
    
    print(f"\n=== 最終結果 ===")
    print(f"保存されたファイル数: {result['submission_count']}")
    print(f"ユニークユーザー数: {result['unique_users']}")
    print(f"処理ページ数: {result['pages_processed']}")
    print(f"出力ディレクトリ: {result['output_directory']}")
