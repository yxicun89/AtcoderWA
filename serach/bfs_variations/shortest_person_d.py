# 最短経路BFS - Person D (複数経路対応版)
from collections import deque

def find_all_shortest_paths(graph_structure, origin, target):
    if origin == target:
        return [[origin]]
    
    visited = {origin}
    queue = deque([(origin, [origin])])
    shortest_paths = []
    shortest_length = None
    
    while queue:
        vertex, path = queue.popleft()
        
        # 既に最短経路より長い場合はスキップ
        if shortest_length is not None and len(path) > shortest_length:
            continue
        
        for neighbor in graph_structure[vertex]:
            new_path = path + [neighbor]
            
            if neighbor == target:
                if shortest_length is None:
                    shortest_length = len(new_path)
                    shortest_paths.append(new_path)
                elif len(new_path) == shortest_length:
                    shortest_paths.append(new_path)
            elif neighbor not in visited or len(new_path) <= shortest_length:
                if neighbor not in visited:
                    visited.add(neighbor)
                queue.append((neighbor, new_path))
    
    return shortest_paths

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'F'], 'D': ['B', 'F'], 'F': ['C', 'D']}
    paths = find_all_shortest_paths(graph, 'A', 'F')
    print(f"All shortest paths from A to F:")
    for i, path in enumerate(paths, 1):
        print(f"  Path {i}: {' → '.join(path)}")
