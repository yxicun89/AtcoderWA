# 幅優先探索 (BFS) - 最短経路探索
from collections import deque

def bfs_shortest_path(graph, start, goal):
    """
    最短経路を探索する幅優先探索の関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param start: 始点ノード
    :param goal: 終点ノード
    :return: 最短経路 (リスト形式)
    """
    visited = set()
    queue = deque([(start, [start])])  # (現在のノード, 経路) をキューに格納
    visited.add(start)

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path  # 経路を返す

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # 経路が見つからない場合

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

    print("Shortest path from 'A' to 'F':")
    path = bfs_shortest_path(graph, 'A', 'F')
    print(path)
