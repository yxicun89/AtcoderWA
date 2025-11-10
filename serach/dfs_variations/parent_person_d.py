# 親ノード追跡DFS - Person D (タプル版)
def dfs_parent_tracking(network, root):
    explored = set()
    
    def dfs_recursive(vertex, predecessor):
        if vertex in explored:
            return []
        
        explored.add(vertex)
        relationships = [(predecessor, vertex)]
        print(f"Relationship: {predecessor} is parent of {vertex}")
        
        for neighbor in network[vertex]:
            if neighbor != predecessor:
                relationships.extend(dfs_recursive(neighbor, vertex))
        
        return relationships
    
    return dfs_recursive(root, None)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    relations = dfs_parent_tracking(graph, 'A')
    print("All parent-child relations:", relations)
