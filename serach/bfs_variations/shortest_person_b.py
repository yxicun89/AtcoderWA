# 最短経路BFS - Person B (親ノード追跡版)
from collections import deque

def find_shortest_route(network, source, destination):
    parent_tracker = {source: None}
    exploration_queue = deque([source])
    
    while exploration_queue:
        current_node = exploration_queue.popleft()
        
        if current_node == destination:
            # 経路を再構築
            route = []
            while current_node is not None:
                route.append(current_node)
                current_node = parent_tracker[current_node]
            return route[::-1]  # 逆順にして正しい順序に
        
        for adjacent_node in network[current_node]:
            if adjacent_node not in parent_tracker:
                parent_tracker[adjacent_node] = current_node
                exploration_queue.append(adjacent_node)
    
    return None  # 経路が見つからない

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'F'], 'D': ['B'], 'F': ['C']}
    route = find_shortest_route(graph, 'A', 'F')
    print(f"Route found: {' -> '.join(route) if route else 'No path'}")
