# 連結成分DFS - Person C (クラス版)
class ComponentFinder:
    def __init__(self, network):
        self.network = network
        self.visited_nodes = set()
        self.component_list = []
    
    def find_all_components(self):
        for vertex in self.network:
            if vertex not in self.visited_nodes:
                current_component = []
                self._explore_component(vertex, current_component)
                self.component_list.append(current_component)
                print(f"Found component: {current_component}")
        
        return self.component_list
    
    def _explore_component(self, node, component):
        self.visited_nodes.add(node)
        component.append(node)
        
        for neighbor in self.network[node]:
            if neighbor not in self.visited_nodes:
                self._explore_component(neighbor, component)

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    finder = ComponentFinder(graph)
    all_components = finder.find_all_components()
    print(f"Total components found: {len(all_components)}")
