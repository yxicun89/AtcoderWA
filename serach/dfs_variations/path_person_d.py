# 経路追跡DFS - Person D (ジェネレータ版)
def path_generator(network, start_node, current_trail=None):
    if current_trail is None:
        current_trail = []
    
    current_trail.append(start_node)
    yield current_trail.copy()
    
    for connected_node in network[start_node]:
        if connected_node not in current_trail:  # 循環を防ぐ
            yield from path_generator(network, connected_node, current_trail)
    
    current_trail.pop()

def display_paths(graph, root):
    for path in path_generator(graph, root):
        path_str = " ↪ ".join(path)
        print(f"Path: {path_str}")

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    display_paths(graph, 'A')
