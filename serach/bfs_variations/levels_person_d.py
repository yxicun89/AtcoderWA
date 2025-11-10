# レベル追跡BFS - Person D (最大レベル付き)
from collections import deque

def max_level_bfs(graph_dict, initial_node):
    max_level = 0
    node_levels = []
    seen_nodes = set()
    processing_queue = deque([(initial_node, 0)])
    seen_nodes.add(initial_node)
    
    while processing_queue:
        current, level = processing_queue.popleft()
        node_levels.append((current, level))
        max_level = max(max_level, level)
        print(f"Processing {current} at level {level}")
        
        for connected in graph_dict[current]:
            if connected not in seen_nodes:
                seen_nodes.add(connected)
                processing_queue.append((connected, level + 1))
    
    print(f"Maximum level reached: {max_level}")
    return node_levels, max_level

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    levels, max_lvl = max_level_bfs(graph, 'A')
    print(f"All node levels: {levels}")
