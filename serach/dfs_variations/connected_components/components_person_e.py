# 連結成分DFS - Person E (統計情報付き)
def comprehensive_component_analysis(network_structure):
    visited_tracker = set()
    component_statistics = {
        'components': [],
        'sizes': [],
        'total_count': 0,
        'largest_size': 0,
        'smallest_size': float('inf')
    }
    
    def recursive_component_builder(node, current_component):
        if node in visited_tracker:
            return
        
        visited_tracker.add(node)
        current_component.append(node)
        
        for connected_node in network_structure[node]:
            if connected_node not in visited_tracker:
                recursive_component_builder(connected_node, current_component)
    
    for node in network_structure:
        if node not in visited_tracker:
            component = []
            recursive_component_builder(node, component)
            
            if component:
                component_size = len(component)
                component_statistics['components'].append(component)
                component_statistics['sizes'].append(component_size)
                component_statistics['largest_size'] = max(component_statistics['largest_size'], component_size)
                component_statistics['smallest_size'] = min(component_statistics['smallest_size'], component_size)
                
                print(f"Component {len(component_statistics['components'])}: {component} (size: {component_size})")
    
    component_statistics['total_count'] = len(component_statistics['components'])
    
    return component_statistics

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    stats = comprehensive_component_analysis(graph)
    print(f"Analysis complete: {stats['total_count']} components, largest: {stats['largest_size']}, smallest: {stats['smallest_size']}")
