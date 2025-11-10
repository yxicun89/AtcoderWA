# 連結成分BFS - Person D (クラス版)
from collections import deque

class ComponentAnalyzer:
    def __init__(self, graph_data):
        self.graph = graph_data
        self.visited_set = set()
        self.components_list = []
        self.largest_component = []
        
    def discover_components(self):
        for vertex in self.graph:
            if vertex not in self.visited_set:
                component = self._bfs_component(vertex)
                self.components_list.append(component)
                
                if len(component) > len(self.largest_component):
                    self.largest_component = component
        
        return self.components_list
    
    def _bfs_component(self, start_vertex):
        component = []
        queue = deque([start_vertex])
        self.visited_set.add(start_vertex)
        
        while queue:
            current = queue.popleft()
            component.append(current)
            
            for neighbor in self.graph[current]:
                if neighbor not in self.visited_set:
                    self.visited_set.add(neighbor)
                    queue.append(neighbor)
        
        print(f"Component discovered: {component}")
        return component
    
    def get_largest_component(self):
        return self.largest_component

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    analyzer = ComponentAnalyzer(graph)
    all_components = analyzer.discover_components()
    largest = analyzer.get_largest_component()
    print(f"Largest component: {largest} (size: {len(largest)})")
