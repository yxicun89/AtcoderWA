# 連結成分BFS - Person E (統計版)
from collections import deque

def comprehensive_component_analysis(network):
    unvisited = set(network.keys())
    component_statistics = {
        'components': [],
        'count': 0,
        'sizes': [],
        'isolated_nodes': [],
        'max_size': 0,
        'min_size': float('inf')
    }
    
    while unvisited:
        start_node = next(iter(unvisited))
        component = []
        search_queue = deque([start_node])
        unvisited.remove(start_node)
        
        while search_queue:
            current_node = search_queue.popleft()
            component.append(current_node)
            
            for neighbor in network[current_node]:
                if neighbor in unvisited:
                    unvisited.remove(neighbor)
                    search_queue.append(neighbor)
        
        # 統計情報を更新
        component_size = len(component)
        component_statistics['components'].append(sorted(component))
        component_statistics['sizes'].append(component_size)
        component_statistics['max_size'] = max(component_statistics['max_size'], component_size)
        component_statistics['min_size'] = min(component_statistics['min_size'], component_size)
        
        if component_size == 1:
            component_statistics['isolated_nodes'].extend(component)
        
        print(f"Component {component_statistics['count'] + 1}: {sorted(component)} (size: {component_size})")
    
    component_statistics['count'] = len(component_statistics['components'])
    return component_statistics

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    stats = comprehensive_component_analysis(graph)
    print(f"\nSummary: {stats['count']} components, sizes: {stats['sizes']}")
    print(f"Isolated nodes: {stats['isolated_nodes']}")
    print(f"Size range: {stats['min_size']} - {stats['max_size']}")
