# 連結成分DFS - Person A (基本実装)
def find_connected_components(graph):
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            component = []
            dfs_collect(graph, node, visited, component)
            components.append(component)
    
    return components

def dfs_collect(graph, node, visited, component):
    visited.add(node)
    component.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_collect(graph, neighbor, visited, component)

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    components = find_connected_components(graph)
    for i, comp in enumerate(components):
        print(f"Component {i+1}: {comp}")
