# 親ノード追跡DFS - Person C (クラス版)
class ParentTrackingDFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.parent_child_pairs = []
    
    def traverse(self, node, parent_node=None):
        if node in self.visited:
            return
            
        self.visited.append(node)
        self.parent_child_pairs.append((parent_node, node))
        print(f"Edge: {parent_node} -> {node}")
        
        for adjacent in self.graph[node]:
            if adjacent != parent_node:
                self.traverse(adjacent, node)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    dfs = ParentTrackingDFS(graph)
    dfs.traverse('A')
    print("All edges:", dfs.parent_child_pairs)
