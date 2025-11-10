# 連結成分BFS - Person A (基本実装)
from collections import deque

def bfs_connected_components(graph):
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

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    components = bfs_connected_components(graph)
    for i, comp in enumerate(components):
        print(f"Component {i+1}: {comp}")
