# 幅優先探索 (BFS) - 連結成分探索
from collections import deque

def bfs_connected_components(graph):
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
            queue = deque([node])
            visited.add(node)

            while queue:
                current = queue.popleft()
                component.append(current)

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            components.append(component)

    return components

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
    components = bfs_connected_components(graph)
    for i, component in enumerate(components):
        print(f"Component {i + 1}: {component}")
