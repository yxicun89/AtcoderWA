# 距離記録BFS - Person C (最大距離付き版)
from collections import deque

def find_max_distance_bfs(adjacency_dict, starting_vertex):
    distance_tracker = {starting_vertex: 0}
    max_distance = 0
    farthest_nodes = [starting_vertex]
    exploration_queue = deque([starting_vertex])
    
    while exploration_queue:
        vertex = exploration_queue.popleft()
        current_dist = distance_tracker[vertex]
        
        for neighbor in adjacency_dict[vertex]:
            if neighbor not in distance_tracker:
                new_distance = current_dist + 1
                distance_tracker[neighbor] = new_distance
                exploration_queue.append(neighbor)
                
                if new_distance > max_distance:
                    max_distance = new_distance
                    farthest_nodes = [neighbor]
                elif new_distance == max_distance:
                    farthest_nodes.append(neighbor)
    
    print(f"Maximum distance: {max_distance}")
    print(f"Farthest nodes: {farthest_nodes}")
    return distance_tracker, max_distance, farthest_nodes

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    distances, max_dist, farthest = find_max_distance_bfs(graph, 'A')
    print(f"All distances: {distances}")
