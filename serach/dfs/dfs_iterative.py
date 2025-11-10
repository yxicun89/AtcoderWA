# 深さ優先探索 (DFS) の別実装 - イテレーティブ版

def dfs_iterative(graph, start):
    """
    深さ優先探索 (DFS) をイテレーティブに実行する関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param start: 探索を開始するノード
    """
    visited = set()  # 訪問済みノードを記録する集合
    stack = [start]  # スタックを使用して探索を管理

    while stack:
        node = stack.pop()  # スタックの最後の要素を取得

        if node not in visited:
            visited.add(node)  # 現在のノードを訪問済みにする
            print(node)  # 訪問したノードを出力

            # 隣接ノードをスタックに追加（未訪問のノードのみ）
            # 逆順に追加することで、次に訪問するノードが正しい順序になる
            stack.extend(reversed(graph[node]))

# 使用例
if __name__ == "__main__":
    # グラフを隣接リストで表現
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # ノード 'A' から探索を開始
    print("Iterative DFS traversal starting from node 'A':")
    dfs_iterative(graph, 'A')
