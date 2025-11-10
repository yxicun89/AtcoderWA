# 最短経路BFS - Person C (距離付き版)
from collections import deque

def shortest_path_with_distance(adjacency_dict, start_vertex, target_vertex):
    visited_nodes = set()
    search_queue = deque([(start_vertex, [start_vertex], 0)])  # (node, path, distance)
    visited_nodes.add(start_vertex)
    
    while search_queue:
        current, current_path, distance = search_queue.popleft()
        
        if current == target_vertex:
            print(f"Target reached! Distance: {distance}")
            return current_path, distance
        
        for neighbor in adjacency_dict[current]:
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                new_path = current_path + [neighbor]
                search_queue.append((neighbor, new_path, distance + 1))
    
    return None, -1  # 経路なし

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'F'], 'D': ['B'], 'F': ['C']}
    path, dist = shortest_path_with_distance(graph, 'A', 'F')
    if path:
        print(f"Path: {' ➔ '.join(path)}, Distance: {dist}")
    else:
        print("No path found")
