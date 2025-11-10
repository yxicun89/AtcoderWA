# 幅優先探索 (BFS) - 基本的な実装
from collections import deque

def bfs(graph, start):
    """
    基本的な幅優先探索を実行する関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param start: 探索を開始するノード
    """
    visited = set()
    queue = deque([start])  # キューを初期化
    visited.add(start)

    while queue:
        node = queue.popleft()  # キューの先頭を取得
        print(node)  # 訪問したノードを出力

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 使用例
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Basic BFS traversal starting from node 'A':")
    bfs(graph, 'A')
