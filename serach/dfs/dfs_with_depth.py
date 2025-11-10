# 深さ優先探索 (DFS) - 深さ追跡付き

def dfs_with_depth(graph, node, depth=0, visited=None):
    """
    深さを追跡しながら深さ優先探索を実行する関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param node: 現在のノード
    :param depth: 現在の深さ
    :param visited: 訪問済みノードを記録する集合
    """
    if visited is None:
        visited = set()

    visited.add(node)
    print(f"Node: {node}, Depth: {depth}")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_with_depth(graph, neighbor, depth + 1, visited)

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

    print("DFS with depth tracking starting from node 'A':")
    dfs_with_depth(graph, 'A')
