# 親ノード追跡DFS - Person A (基本実装)
def dfs_with_parent(graph, node, parent=None, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(f"Node: {node}, Parent: {parent}")
    
    for neighbor in graph[node]:
        if neighbor != parent and neighbor not in visited:
            dfs_with_parent(graph, neighbor, node, visited)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    dfs_with_parent(graph, 'A')
