# 再帰的DFS - Person E (辞書返却版)
def depth_first_search(adjacency_list, starting_node):
    exploration_status = {}
    
    def explore(current_node):
        exploration_status[current_node] = True
        print(f"Explored: {current_node}")
        
        for connected_node in adjacency_list[current_node]:
            if connected_node not in exploration_status:
                explore(connected_node)
    
    explore(starting_node)
    return exploration_status

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    visited_dict = depth_first_search(graph, 'A')
    print("Exploration completed:", visited_dict)
