# 最短経路BFS - Person A (基本実装)
from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)
    
    while queue:
        node, path = queue.popleft()
        
        if node == goal:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'F'], 'D': ['B'], 'F': ['C']}
    path = bfs_shortest_path(graph, 'A', 'F')
    print(f"Shortest path from A to F: {path}")
