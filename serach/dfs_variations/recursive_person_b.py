# 再帰的DFS - Person B (リスト返却版)
def dfs_recursive(graph, start):
    visited = []
    
    def dfs_helper(node):
        if node in visited:
            return
        visited.append(node)
        for neighbor in graph[node]:
            dfs_helper(neighbor)
    
    dfs_helper(start)
    return visited

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    result = dfs_recursive(graph, 'A')
    print("Visited nodes:", result)
