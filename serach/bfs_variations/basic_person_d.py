# 基本BFS - Person D (ジェネレータ版)
from collections import deque

def bfs_generator(graph_structure, root):
    seen = set()
    queue = deque([root])
    seen.add(root)
    
    while queue:
        vertex = queue.popleft()
        yield vertex
        
        for connected in graph_structure[vertex]:
            if connected not in seen:
                seen.add(connected)
                queue.append(connected)

def run_bfs_with_generator(graph, start):
    print("BFS traversal using generator:")
    for node in bfs_generator(graph, start):
        print(f"Generated: {node}")

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    run_bfs_with_generator(graph, 'A')
