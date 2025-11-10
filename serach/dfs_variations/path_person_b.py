# 経路追跡DFS - Person B (全経路収集版)
def collect_all_paths(graph, start):
    all_paths = []
    visited = set()
    
    def path_finder(node, current_path):
        visited.add(node)
        current_path.append(node)
        
        has_unvisited_neighbors = False
        for neighbor in graph[node]:
            if neighbor not in visited:
                has_unvisited_neighbors = True
                path_finder(neighbor, current_path.copy())
        
        if not has_unvisited_neighbors:
            all_paths.append(current_path.copy())
            print(f"Complete path: {' → '.join(current_path)}")
        
        visited.remove(node)
    
    path_finder(start, [])
    return all_paths

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    paths = collect_all_paths(graph, 'A')
    print(f"Total paths found: {len(paths)}")
