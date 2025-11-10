# 基本BFS - Person C (クラス版)
from collections import deque

class BFSTraversal:
    def __init__(self, network):
        self.network = network
        self.visited_nodes = set()
        self.traversal_order = []
    
    def traverse(self, start_vertex):
        node_queue = deque([start_vertex])
        self.visited_nodes.add(start_vertex)
        
        while node_queue:
            current_vertex = node_queue.popleft()
            self.traversal_order.append(current_vertex)
            print(f"Processing vertex: {current_vertex}")
            
            for adjacent_vertex in self.network[current_vertex]:
                if adjacent_vertex not in self.visited_nodes:
                    self.visited_nodes.add(adjacent_vertex)
                    node_queue.append(adjacent_vertex)
        
        return self.traversal_order

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    bfs_obj = BFSTraversal(graph)
    order = bfs_obj.traverse('A')
    print("Final order:", order)
