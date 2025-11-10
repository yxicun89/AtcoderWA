# 深さ追跡DFS - Person C (イテレーティブ版)
def iterative_depth_dfs(graph, root):
    visited = set()
    stack = [(root, 0)]  # (node, depth)のタプル
    depth_record = {}
    
    while stack:
        node, level = stack.pop()
        
        if node not in visited:
            visited.add(node)
            depth_record[node] = level
            print(f"Processing {node} at depth {level}")
            
            # 隣接ノードを逆順で追加（正しい順序のため）
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, level + 1))
    
    return depth_record

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    result = iterative_depth_dfs(graph, 'A')
    print("Depth results:", result)
