# イテレーティブDFS - Person D (try-except版)
def stack_dfs(graph_dict, start_vertex):
    seen = []
    stack = [start_vertex]
    
    while len(stack) > 0:
        try:
            current_vertex = stack.pop()
            
            if current_vertex not in seen:
                seen.append(current_vertex)
                print(f"Found: {current_vertex}")
                
                # 隣接頂点をスタックに追加
                neighbors = graph_dict.get(current_vertex, [])
                for vertex in neighbors:
                    stack.append(vertex)
                    
        except IndexError:
            break
    
    return seen

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    visited = stack_dfs(graph, 'A')
    print("Traversal complete:", visited)
