# 連結成分DFS - Person D (イテレーティブ版)
def iterative_component_detection(graph_dict):
    seen_vertices = set()
    component_groups = []
    
    for starting_vertex in graph_dict:
        if starting_vertex not in seen_vertices:
            current_group = []
            vertex_stack = [starting_vertex]
            
            while vertex_stack:
                vertex = vertex_stack.pop()
                
                if vertex not in seen_vertices:
                    seen_vertices.add(vertex)
                    current_group.append(vertex)
                    
                    # 隣接する未訪問の頂点をスタックに追加
                    for adjacent in graph_dict[vertex]:
                        if adjacent not in seen_vertices:
                            vertex_stack.append(adjacent)
            
            if current_group:
                component_groups.append(sorted(current_group))
                print(f"Component detected: {sorted(current_group)}")
    
    return component_groups

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    groups = iterative_component_detection(graph)
    print(f"All component groups: {groups}")
