# 基本BFS - Person E (関数型版)
from collections import deque

def functional_bfs(adjacency_dict, start_node):
    def bfs_step(queue, visited):
        if not queue:
            return visited
        
        current = queue.popleft()
        new_visited = visited | {current}
        print(f"Node encountered: {current}")
        
        # 新しい隣接ノードをキューに追加
        new_neighbors = [n for n in adjacency_dict[current] if n not in new_visited and n not in queue]
        queue.extend(new_neighbors)
        
        return bfs_step(queue, new_visited)
    
    initial_queue = deque([start_node])
    return bfs_step(initial_queue, set())

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    visited_set = functional_bfs(graph, 'A')
    print("All visited nodes:", visited_set)
