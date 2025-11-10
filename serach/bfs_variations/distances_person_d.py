# 距離記録BFS - Person D (距離グループ版)
from collections import deque, defaultdict

def group_nodes_by_distance(graph_structure, root_node):
    distance_groups = defaultdict(list)
    node_distances = {root_node: 0}
    search_queue = deque([root_node])
    
    while search_queue:
        current = search_queue.popleft()
        current_distance = node_distances[current]
        distance_groups[current_distance].append(current)
        
        for adjacent in graph_structure[current]:
            if adjacent not in node_distances:
                node_distances[adjacent] = current_distance + 1
                search_queue.append(adjacent)
    
    # 距離グループを表示
    for distance in sorted(distance_groups.keys()):
        nodes_at_distance = distance_groups[distance]
        print(f"Distance {distance}: {nodes_at_distance}")
    
    return dict(distance_groups), node_distances

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    groups, distances = group_nodes_by_distance(graph, 'A')
    print(f"Distance groups: {groups}")
    print(f"Individual distances: {distances}")
