# 深さ優先探索 (DFS) - 再帰的実装

def dfs_recursive(graph, node, visited=None):
    """
    再帰的に深さ優先探索を実行する関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param node: 現在のノード
    :param visited: 訪問済みノードを記録する集合
    """
    if visited is None:
        visited = set()

    visited.add(node)
    print(node)  # 訪問したノードを出力

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

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

    print("Recursive DFS traversal starting from node 'A':")
    dfs_recursive(graph, 'A')
