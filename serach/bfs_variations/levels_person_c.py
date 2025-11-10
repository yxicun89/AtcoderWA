# レベル追跡BFS - Person C (レベル別処理版)
from collections import deque, defaultdict

def bfs_by_levels(adjacency_list, starting_vertex):
    levels = defaultdict(list)
    visited = set()
    queue = deque([(starting_vertex, 0)])
    visited.add(starting_vertex)
    
    while queue:
        vertex, depth = queue.popleft()
        levels[depth].append(vertex)
        
        for neighbor in adjacency_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    
    # レベルごとに表示
    for level, nodes in levels.items():
        print(f"Level {level}: {nodes}")
    
    return dict(levels)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    level_dict = bfs_by_levels(graph, 'A')
    print("Complete level structure:", level_dict)
