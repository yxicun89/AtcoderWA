# 経路追跡DFS - Person C (イテレーティブ版)
def iterative_path_tracking(adjacency_list, root):
    stack = [(root, [root])]  # (current_node, path_to_node)
    visited = set()
    
    while stack:
        vertex, route = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            print(f"Current route: {' ▶ '.join(route)}")
            
            # 隣接ノードを逆順で追加
            for next_vertex in reversed(adjacency_list[vertex]):
                if next_vertex not in visited:
                    new_route = route + [next_vertex]
                    stack.append((next_vertex, new_route))

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    iterative_path_tracking(graph, 'A')
