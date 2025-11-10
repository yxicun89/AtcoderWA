# 連結成分BFS - Person C (サイズ付き版)
from collections import deque

def find_components_with_sizes(adjacency_list):
    seen = set()
    component_info = []
    
    for starting_node in adjacency_list:
        if starting_node not in seen:
            component_nodes = []
            exploration_queue = deque([starting_node])
            seen.add(starting_node)
            
            while exploration_queue:
                node = exploration_queue.popleft()
                component_nodes.append(node)
                
                for connected_node in adjacency_list[node]:
                    if connected_node not in seen:
                        seen.add(connected_node)
                        exploration_queue.append(connected_node)
            
            component_size = len(component_nodes)
            component_info.append({
                'nodes': sorted(component_nodes),
                'size': component_size
            })
            print(f"Found component of size {component_size}: {sorted(component_nodes)}")
    
    return component_info

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    info = find_components_with_sizes(graph)
    total_nodes = sum(comp['size'] for comp in info)
    print(f"Total components: {len(info)}, Total nodes: {total_nodes}")
