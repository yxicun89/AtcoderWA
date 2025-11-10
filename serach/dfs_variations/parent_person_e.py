# 親ノード追跡DFS - Person E (ジェネレータ版)
def parent_aware_dfs(graph, start, parent=None):
    yield (parent, start)
    print(f"Yielding: parent={parent}, current={start}")
    
    for neighbor in graph[start]:
        if neighbor != parent:
            yield from parent_aware_dfs(graph, neighbor, start)

def collect_parent_info(graph, root):
    parent_info = {}
    for parent, child in parent_aware_dfs(graph, root):
        parent_info[child] = parent
    return parent_info

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    info = collect_parent_info(graph, 'A')
    print("Parent information:", info)
