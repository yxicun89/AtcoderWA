# 距離記録BFS - Person A (基本実装)
from collections import deque

def bfs_with_distances(graph, start):
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    distances = bfs_with_distances(graph, 'A')
    for node, dist in distances.items():
        print(f"Distance to {node}: {dist}")
