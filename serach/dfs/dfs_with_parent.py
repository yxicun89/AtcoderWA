# 深さ優先探索 (DFS) - 親ノード追跡付き

def dfs_with_parent(graph, node, parent=None, visited=None):
    """
    親ノードを追跡しながら深さ優先探索を実行する関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param node: 現在のノード
    :param parent: 親ノード
    :param visited: 訪問済みノードを記録する集合
    """
    if visited is None:
        visited = set()

    visited.add(node)
    print(f"Node: {node}, Parent: {parent}")

    for neighbor in graph[node]:
        if neighbor != parent:  # 親ノードを無視
            dfs_with_parent(graph, neighbor, node, visited)

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

    print("DFS with parent tracking starting from node 'A':")
    dfs_with_parent(graph, 'A')
