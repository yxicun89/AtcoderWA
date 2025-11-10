# 深さ追跡DFS - Person E (クラス版インデント表示)
class DepthVisualizer:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list
        self.visited_nodes = set()
    
    def visualize_depth(self, node, level=0):
        if node in self.visited_nodes:
            return
        
        self.visited_nodes.add(node)
        indent = "  " * level
        print(f"{indent}├─ {node} (depth: {level})")
        
        for child in self.graph[node]:
            if child not in self.visited_nodes:
                self.visualize_depth(child, level + 1)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    visualizer = DepthVisualizer(graph)
    print("Tree visualization:")
    visualizer.visualize_depth('A')
