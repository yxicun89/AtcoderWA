# 経路追跡DFS - Person A (基本実装)
def dfs_with_path(graph, node, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(node)
    path.append(node)
    print(" -> ".join(path))
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_with_path(graph, neighbor, path, visited)
    
    path.pop()

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    dfs_with_path(graph, 'A')
