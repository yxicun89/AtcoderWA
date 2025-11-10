# レベル追跡BFS - Person A (基本実装)
from collections import deque

def bfs_with_levels(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    
    while queue:
        node, level = queue.popleft()
        print(f"Node: {node}, Level: {level}")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    bfs_with_levels(graph, 'A')
