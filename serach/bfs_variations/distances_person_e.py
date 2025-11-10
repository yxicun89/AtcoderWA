# 距離記録BFS - Person E (クラス版統計付き)
from collections import deque

class DistanceCalculator:
    def __init__(self, network):
        self.network = network
        self.distance_data = {}
        self.statistics = {}
    
    def compute_distances(self, origin_node):
        self.distance_data = {origin_node: 0}
        processing_queue = deque([origin_node])
        
        while processing_queue:
            current_node = processing_queue.popleft()
            
            for neighbor_node in self.network[current_node]:
                if neighbor_node not in self.distance_data:
                    self.distance_data[neighbor_node] = self.distance_data[current_node] + 1
                    processing_queue.append(neighbor_node)
        
        self._calculate_statistics()
        return self.distance_data
    
    def _calculate_statistics(self):
        distances = list(self.distance_data.values())
        self.statistics = {
            'total_nodes': len(distances),
            'max_distance': max(distances),
            'min_distance': min(distances),
            'average_distance': sum(distances) / len(distances)
        }
    
    def get_statistics(self):
        return self.statistics
    
    def print_summary(self):
        print("Distance Summary:")
        for node, distance in sorted(self.distance_data.items()):
            print(f"  {node}: {distance}")
        print(f"Statistics: {self.statistics}")

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    calculator = DistanceCalculator(graph)
    distances = calculator.compute_distances('A')
    calculator.print_summary()
