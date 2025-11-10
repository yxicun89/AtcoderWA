# 基本BFS - Person B (リスト版)
def breadth_first_search(adjacency_list, starting_node):
    explored = []
    to_explore = [starting_node]
    
    while to_explore:
        current = to_explore.pop(0)  # FIFOのためpop(0)を使用
        
        if current not in explored:
            explored.append(current)
            print(f"Visited: {current}")
            
            for neighbor in adjacency_list[current]:
                if neighbor not in explored and neighbor not in to_explore:
                    to_explore.append(neighbor)
    
    return explored

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    result = breadth_first_search(graph, 'A')
    print("Exploration order:", result)
