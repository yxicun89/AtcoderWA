# イテレーティブDFS - Person E (関数型スタイル)
def dfs_functional(graph, start):
    def process_node(stack, visited):
        if not stack:
            return visited
        
        node = stack.pop()
        if node in visited:
            return process_node(stack, visited)
        
        new_visited = visited | {node}
        print(f"Node processed: {node}")
        
        # 新しいノードをスタックに追加
        new_stack = stack + [n for n in graph[node] if n not in new_visited]
        return process_node(new_stack, new_visited)
    
    return process_node([start], set())

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    result = dfs_functional(graph, 'A')
    print("Final visited set:", result)
