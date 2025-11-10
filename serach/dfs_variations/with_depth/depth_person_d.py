# 深さ追跡DFS - Person D (最大深度付き)
def max_depth_dfs(network, start_node):
    max_depth = 0
    visited_with_depth = []
    seen = set()
    
    def explore_depth(vertex, depth):
        nonlocal max_depth
        
        if vertex in seen:
            return
        
        seen.add(vertex)
        visited_with_depth.append((vertex, depth))
        max_depth = max(max_depth, depth)
        print(f"Vertex {vertex} found at depth {depth}")
        
        for next_vertex in network[vertex]:
            if next_vertex not in seen:
                explore_depth(next_vertex, depth + 1)
    
    explore_depth(start_node, 0)
    print(f"Maximum depth reached: {max_depth}")
    return visited_with_depth, max_depth

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    visits, max_d = max_depth_dfs(graph, 'A')
    print("Visits with depth:", visits)
