# 深さ追跡DFS - Person A (基本実装)
def dfs_with_depth(graph, node, depth=0, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(f"Node: {node}, Depth: {depth}")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_with_depth(graph, neighbor, depth + 1, visited)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    dfs_with_depth(graph, 'A')
