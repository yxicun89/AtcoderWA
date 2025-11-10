# 再帰的DFS - Person C (クラス実装)
class DFSTraversal:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        
    def dfs(self, node):
        self.visited.add(node)
        print(f"Visiting: {node}")
        for adjacent in self.graph[node]:
            if adjacent not in self.visited:
                self.dfs(adjacent)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    traversal = DFSTraversal(graph)
    traversal.dfs('A')
