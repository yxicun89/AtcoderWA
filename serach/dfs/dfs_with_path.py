# 深さ優先探索 (DFS) - 経路追跡付き

def dfs_with_path(graph, node, path=None, visited=None):
    """
    経路を追跡しながら深さ優先探索を実行する関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param node: 現在のノード
    :param path: 現在の探索経路
    :param visited: 訪問済みノードを記録する集合
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    path.append(node)
    print(" -> ".join(path))

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_with_path(graph, neighbor, path, visited)

    path.pop()  # 戻るときに経路を削除

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

    print("DFS with path tracking starting from node 'A':")
    dfs_with_path(graph, 'A')
