# 最短経路BFS - Person E (クラス版)
from collections import deque

class ShortestPathFinder:
    def __init__(self, network):
        self.network = network
        self.search_history = []
    
    def find_path(self, start_node, end_node):
        if start_node == end_node:
            return [start_node]
        
        discovered = {start_node}
        path_queue = deque([(start_node, [start_node])])
        
        while path_queue:
            current_node, current_route = path_queue.popleft()
            self.search_history.append(current_node)
            
            for connected_node in self.network[current_node]:
                if connected_node == end_node:
                    final_path = current_route + [connected_node]
                    print(f"Path discovered: {' ⟶ '.join(final_path)}")
                    return final_path
                
                if connected_node not in discovered:
                    discovered.add(connected_node)
                    extended_route = current_route + [connected_node]
                    path_queue.append((connected_node, extended_route))
        
        return None  # 経路なし
    
    def get_search_history(self):
        return self.search_history

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'F'], 'D': ['B'], 'F': ['C']}
    finder = ShortestPathFinder(graph)
    result = finder.find_path('A', 'F')
    if result:
        print(f"Final result: {result}")
    print(f"Search history: {finder.get_search_history()}")
