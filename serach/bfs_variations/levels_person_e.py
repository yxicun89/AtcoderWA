# レベル追跡BFS - Person E (視覚化版)
from collections import deque

class LevelVisualizer:
    def __init__(self, network):
        self.network = network
        self.level_info = {}
    
    def visualize_levels(self, root):
        queue = deque([(root, 0)])
        self.level_info[root] = 0
        
        while queue:
            node, level = queue.popleft()
            indent = "  " * level
            print(f"{indent}Level {level}: {node}")
            
            for child in self.network[node]:
                if child not in self.level_info:
                    self.level_info[child] = level + 1
                    queue.append((child, level + 1))
        
        return self.level_info

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    visualizer = LevelVisualizer(graph)
    print("Level visualization:")
    info = visualizer.visualize_levels('A')
    print("Level information:", info)
