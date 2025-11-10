# 幅優先探索 (BFS) - レベル追跡付き
from collections import deque

def bfs_with_levels(graph, start):
    """
    レベルを追跡しながら幅優先探索を実行する関数。

    :param graph: 隣接リストで表現されたグラフ (辞書形式)
    :param start: 探索を開始するノード
    """
    visited = set()
    queue = deque([(start, 0)])  # (ノード, レベル) をキューに格納
    visited.add(start)

    while queue:
        node, level = queue.popleft()
        print(f"Node: {node}, Level: {level}")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

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

    print("BFS with levels starting from node 'A':")
    bfs_with_levels(graph, 'A')
