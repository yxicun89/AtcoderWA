# イテレーティブDFS - Person C (while True版)
def dfs_stack_based(network, initial_node):
    visited_nodes = set()
    node_stack = [initial_node]
    
    while True:
        if not node_stack:
            break
            
        vertex = node_stack.pop()
        
        if vertex in visited_nodes:
            continue
            
        visited_nodes.add(vertex)
        print(f"Visit: {vertex}")
        
        # 隣接ノードを逆順で追加
        for adj in reversed(network[vertex]):
            if adj not in visited_nodes:
                node_stack.append(adj)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    dfs_stack_based(graph, 'A')
