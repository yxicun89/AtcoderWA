# 再帰的DFS - Person D (ジェネレータ版)
def dfs_generator(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    if start not in visited:
        visited.add(start)
        yield start
        
        for neighbor in graph[start]:
            yield from dfs_generator(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    for node in dfs_generator(graph, 'A'):
        print(f"Node: {node}")
