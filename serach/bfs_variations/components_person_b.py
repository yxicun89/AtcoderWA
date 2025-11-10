# 連結成分BFS - Person B (辞書版)
from collections import deque

def analyze_connectivity(network_structure):
    explored_vertices = set()
    component_mapping = {}
    component_id = 0
    
    for vertex in network_structure:
        if vertex not in explored_vertices:
            current_component = []
            vertex_queue = deque([vertex])
            explored_vertices.add(vertex)
            
            while vertex_queue:
                current_vertex = vertex_queue.popleft()
                current_component.append(current_vertex)
                component_mapping[current_vertex] = component_id
                
                for adjacent_vertex in network_structure[current_vertex]:
                    if adjacent_vertex not in explored_vertices:
                        explored_vertices.add(adjacent_vertex)
                        vertex_queue.append(adjacent_vertex)
            
            print(f"Component {component_id}: {current_component}")
            component_id += 1
    
    return component_mapping

if __name__ == "__main__":
    graph = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    mapping = analyze_connectivity(graph)
    print("Component mapping:", mapping)
