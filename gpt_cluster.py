# これはbiの間違いカテゴリ

# カテゴリの種類数何個表示させるのがいいのかな問題

# 1. 入力の境界値処理のミス
# 2. 山札の初期状態の誤解
# 3. 操作の条件分岐や順序の実装ミス
# 4. 山札のインデックス範囲外アクセス
# 5. 操作種別 (ti) の不正な値処理
# 6. 出力フォーマットのミス
# 7. 効率性の問題（計算量の最適化不足）
# 8. データ構造の選択ミス
# 9. 空の山札に対する操作エラー

# bi_cluster_categories = {
#     "1": "入力の境界値処理のミス",
#     "2": "山札の初期状態の誤解",
#     "3": "操作の条件分岐や順序の実装ミス",
#     "4": "山札のインデックス範囲外アクセス",
#     "5": "操作種別 (ti) の不正な値処理",
#     "6": "出力フォーマットのミス",
#     "7": "効率性の問題（計算量の最適化不足）",
#     "8": "データ構造の選択ミス",
#     "9": "空の山札に対する操作エラー"
# }

# このコードの間違いを教えてください
# 最後に以下のカテゴリのどれに当たるか数字のみ出力してください

# 1.入力形式の誤解
# 2.8進数と9進数の変換ミス
# 3.数字の置換処理のミス
# 4.K回の操作回数の管理ミス
# 5.出力形式の誤り
# 6.大きな数値の扱いミス
# 7.無限ループや計算量の問題
# 8.境界値処理の不足
# 9.例外処理の不足

# # プロンプト最終
# このコードの間違いを教えてください
# 最後に以下のカテゴリのどれに当たるか数字のみ出力してください
# 間違いの説明とカテゴリの出力のみ出力してください

# 1.入力形式の誤解
# 2.8進数と9進数の変換ミス
# 3.数字の置換処理のミス
# 4.K回の操作回数の管理ミス
# 5.出力形式の誤り
# 6.大きな数値の扱いミス
# 7.無限ループや計算量の問題
# 8.境界値処理の不足
# 9.例外処理の不足


# bi_submission_labels = {

# }

# モデル選定
# GPT 4o
# 理由 github copilotで無料で使えるから+高性能だから


# # 間違いカテゴリプロンプト
# 以下の問題があります
# この問題で起こりそう間違いのカテゴリを箇条書きでタイトルだけ教えて

# 67 base bo
# 8進数の整数Nに対して「Nを9進数にして8を5に置き換える」処理をK回行う
# 操作後の8進数を出力




bo_cluster_categories = {
    "1": "入力形式の誤解",
    "2": "8進数と9進数の変換ミス",
    "3": "数字の置換処理のミス",
    "4": "K回の操作回数の管理ミス",
    "5": "出力形式の誤り",
    "6": "大きな数値の扱いミス",
    "7": "無限ループや計算量の問題",
    "8": "境界値処理の不足",
    "9": "例外処理の不足"
}

bo_submission_labels = {
    "submission_1": "3",
    "submission_2": "4",
    "submission_3": "8",
    "submission_4": "8",
    "submission_5": "6",
    "submission_6": "3",
    "submission_7": "8",
    "submission_8": "8",
    "submission_9": "8",
    "submission_10": "8",
    "submission_11": "8",
    "submission_12": "2",
    "submission_13": "2",
    "submission_14": "8",
    "submission_15": "8",
    "submission_16": "8",
    "submission_17": "6",
    "submission_18": "2",
    "submission_19": "2",
    "submission_20": "7",
    "submission_21": "8",
    "submission_22": "8",
    "submission_23": "8",
    "submission_24": "2",
    "submission_25": "8",
    "submission_26": "2",
    "submission_27": "2",
    "submission_28": "5",
    "submission_29": "2",
    "submission_30": "6",
    "submission_31": "8",
    "submission_32": "8",
    "submission_33": "8",
    "submission_34": "8",
    "submission_35": "4",
    "submission_36": "8",
    "submission_37": "7",
    "submission_38": "2",
    "submission_39": "7",
    "submission_40": "2",
    "submission_41": "2",
    "submission_42": "8",
    "submission_43": "8",
    "submission_44": "5",
    "submission_45": "6",
    "submission_46": "8",
    "submission_47": "8",
    "submission_48": "8",
    "submission_49": "4",
    "submission_50": "8",
    "submission_51": "2",
    "submission_52": "8",
    "submission_53": "2",
    "submission_54": "8",
    "submission_55": "8",
    "submission_56": "7",
    "submission_57": "8",
    "submission_58": "2",
    "submission_59": "8",
    "submission_60": "6",
    "submission_61": "6",
    "submission_62": "8",
    "submission_63": "8",
    "submission_64": "8",
    "submission_65": "8",
    "submission_66": "8",
    "submission_67": "6",
    "submission_68": "4",
    "submission_69": "2",
    "submission_70": "1", #このコードカテゴリのバグ複数持ってるから分類ムズイ
    "submission_71": "8", #このコードも複数カテゴリのバグ持ってるから分類ムズイ
    "submission_72": "2", #2 or 3
    "submission_73": "8",
    "submission_74": "8",
    "submission_75": "4",
    "submission_76": "2",
    "submission_78": "2",
    "submission_79": "2",
    "submission_80": "2",
    "submission_81": "2",
    "submission_82": "6",
    "submission_83": "6",
    "submission_84": "6",
    "submission_85": "4",
    "submission_86": "8",
    "submission_87": "6",
    "submission_88": "8",
    "submission_89": "8",
    "submission_90": "8",
    "submission_91": "8",
    "submission_92": "8",
    "submission_93": "2",
    "submission_94": "3",
    "submission_95": "8",
    "submission_96": "2",
    "submission_97": "1", #複数カテゴリのバグ持ってるから分類ムズイ
    "submission_98": "8",
    "submission_99": "2",
    "submission_100": "8",
}

import os
import shutil

def organize_files_by_category(source_directory, categories, submission_labels):
    """
    指定されたディレクトリのファイルをカテゴリごとに仕分けする

    Args:
        source_directory (str): 元のディレクトリパス
        categories (dict): カテゴリの辞書（key: カテゴリ番号, value: カテゴリ名）
        submission_labels (dict): ファイルとカテゴリの対応（key: ファイル名（.py無し）, value: カテゴリ番号）
    """
    # 出力ディレクトリを作成
    output_directory = source_directory + "_gpt_cluster"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"作成されたディレクトリ: {output_directory}")

    # カテゴリディレクトリを作成
    category_dirs = {}
    for key, value in categories.items():
        category_dir = os.path.join(output_directory, f"pattern_{key}_{value}")
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
            print(f"作成されたカテゴリディレクトリ: {category_dir}")
        category_dirs[key] = category_dir

    # ファイルを仕分け
    for filename, category_id in submission_labels.items():
        source_file = os.path.join(source_directory, f"{filename}.py")

        if os.path.exists(source_file):
            if category_id in category_dirs:
                destination_file = os.path.join(category_dirs[category_id], f"{filename}.py")
                shutil.copy2(source_file, destination_file)
                print(f"コピー完了: {source_file} -> {destination_file}")
            else:
                print(f"警告: カテゴリID '{category_id}' が見つかりません - ファイル: {filename}")
        else:
            print(f"警告: ファイルが見つかりません - {source_file}")

def main():
    """
    メイン処理
    ユーザーに対象ディレクトリを入力してもらい、ファイルの仕分けを実行
    """
    print("ファイル仕分けツール")
    print("=" * 50)

    # ディレクトリの入力
    source_directory = input("対象ディレクトリのパスを入力してください: ").strip()

    if not os.path.exists(source_directory):
        print(f"エラー: ディレクトリ '{source_directory}' が見つかりません")
        return

    print(f"\n対象ディレクトリ: {source_directory}")
    print(f"出力ディレクトリ: {source_directory}_gpt_cluster")

    # 仕分け処理の実行
    organize_files_by_category(source_directory, bo_cluster_categories, bo_submission_labels)

    print("\n仕分け処理が完了しました！")

if __name__ == "__main__":
    main()



