# 幅優先探索 (BFS) - 距離記録付き
from collections import deque

def bfs_with_distances(graph, start):
    """
    距離を記録しながら幅優先探索を実行する関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param start: 探索を開始するノード
    :return: 各ノードまでの距離を記録した辞書
    """
    distances = {start: 0}  # 距離を記録
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in distances:  # 未訪問のノード
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return distances

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

    print("Distances from node 'A':")
    distances = bfs_with_distances(graph, 'A')
    for node, distance in distances.items():
        print(f"Node {node}: {distance}")
