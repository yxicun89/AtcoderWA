# 深さ追跡DFS - Person B (辞書返却版)
def depth_tracking_dfs(adjacency_dict, starting_vertex):
    depth_map = {}
    explored = set()
    
    def traverse_with_level(vertex, current_level):
        if vertex in explored:
            return
        
        explored.add(vertex)
        depth_map[vertex] = current_level
        print(f"Level {current_level}: {vertex}")
        
        for connected_vertex in adjacency_dict[vertex]:
            if connected_vertex not in explored:
                traverse_with_level(connected_vertex, current_level + 1)
    
    traverse_with_level(starting_vertex, 0)
    return depth_map

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    depths = depth_tracking_dfs(graph, 'A')
    print("Depth mapping:", depths)
