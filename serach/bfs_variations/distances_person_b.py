# 距離記録BFS - Person B (詳細版)
from collections import deque

def calculate_node_distances(network, origin):
    distance_map = {}
    visited_order = []
    processing_queue = deque([origin])
    distance_map[origin] = 0
    
    while processing_queue:
        current_node = processing_queue.popleft()
        visited_order.append(current_node)
        current_distance = distance_map[current_node]
        
        print(f"Processing {current_node} (distance: {current_distance})")
        
        for connected_node in network[current_node]:
            if connected_node not in distance_map:
                distance_map[connected_node] = current_distance + 1
                processing_queue.append(connected_node)
    
    return distance_map, visited_order

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    distances, order = calculate_node_distances(graph, 'A')
    print(f"Visit order: {order}")
    print(f"Distance mapping: {distances}")
