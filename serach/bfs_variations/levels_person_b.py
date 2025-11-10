# レベル追跡BFS - Person B (辞書版)
from collections import deque

def level_tracking_bfs(network, root_node):
    depth_map = {root_node: 0}
    exploration_queue = deque([root_node])
    
    while exploration_queue:
        current_node = exploration_queue.popleft()
        current_depth = depth_map[current_node]
        print(f"Exploring {current_node} at depth {current_depth}")
        
        for adjacent_node in network[current_node]:
            if adjacent_node not in depth_map:
                depth_map[adjacent_node] = current_depth + 1
                exploration_queue.append(adjacent_node)
    
    return depth_map

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    depths = level_tracking_bfs(graph, 'A')
    print("Depth mapping:", depths)
