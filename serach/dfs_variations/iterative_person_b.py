# イテレーティブDFS - Person B (collections.deque使用)
from collections import deque

def iterative_dfs(adj_graph, root):
    explored = []
    to_explore = deque([root])
    
    while to_explore:
        current = to_explore.pop()
        if current not in explored:
            explored.append(current)
            print(f"Processing: {current}")
            # 逆順に追加して正しい順序にする
            for neighbor in reversed(adj_graph[current]):
                if neighbor not in explored:
                    to_explore.append(neighbor)
    
    return explored

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    result = iterative_dfs(graph, 'A')
    print("Final result:", result)
