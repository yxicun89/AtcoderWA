# 深さ優先探索 (DFS) - 連結成分探索

def find_connected_components(graph):
    """
    グラフの連結成分を探索する関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :return: 連結成分のリスト
    """
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs_collect(graph, node, visited, component)
            components.append(component)

    return components

def dfs_collect(graph, node, visited, component):
    """
    連結成分を収集するための補助関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param node: 現在のノード
    :param visited: 訪問済みノードを記録する集合
    :param component: 現在の連結成分
    """
    visited.add(node)
    component.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_collect(graph, neighbor, visited, component)

# 使用例
if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B'],
        'D': ['E'],
        'E': ['D'],
        'F': []
    }

    print("Connected components in the graph:")
    components = find_connected_components(graph)
    for i, component in enumerate(components):
        print(f"Component {i + 1}: {component}")
