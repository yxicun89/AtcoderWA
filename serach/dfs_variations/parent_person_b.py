# 親ノード追跡DFS - Person B (辞書版)
def track_parent_dfs(adj_list, start):
    parent_map = {start: None}
    visited = set()
    
    def explore(current, prev):
        visited.add(current)
        parent_map[current] = prev
        print(f"Visiting {current} (came from {prev})")
        
        for next_node in adj_list[current]:
            if next_node not in visited:
                explore(next_node, current)
    
    explore(start, None)
    return parent_map

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    parents = track_parent_dfs(graph, 'A')
    print("Parent mapping:", parents)
