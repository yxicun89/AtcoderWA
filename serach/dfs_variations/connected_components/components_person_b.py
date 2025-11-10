# 連結成分DFS - Person B (辞書返却版)
def analyze_graph_components(adjacency_structure):
    exploration_status = {}
    component_mapping = {}
    component_id = 0
    
    def mark_component(vertex, comp_id):
        if vertex in exploration_status:
            return
        
        exploration_status[vertex] = True
        component_mapping[vertex] = comp_id
        print(f"Node {vertex} belongs to component {comp_id}")
        
        for connected_vertex in adjacency_structure[vertex]:
            mark_component(connected_vertex, comp_id)
    
    for vertex in adjacency_structure:
        if vertex not in exploration_status:
            mark_component(vertex, component_id)
            component_id += 1
    
    return component_mapping

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    mapping = analyze_graph_components(graph)
    print("Component mapping:", mapping)
