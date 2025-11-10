# 経路追跡DFS - Person E (クラス版)
class PathTracker:
    def __init__(self, graph_structure):
        self.graph = graph_structure
        self.journey_log = []
        self.current_journey = []
        self.visited_set = set()
    
    def explore_with_tracking(self, node):
        self.current_journey.append(node)
        self.visited_set.add(node)
        
        journey_string = " ➜ ".join(self.current_journey)
        print(f"Journey: {journey_string}")
        self.journey_log.append(journey_string)
        
        for neighbor in self.graph[node]:
            if neighbor not in self.visited_set:
                self.explore_with_tracking(neighbor)
        
        self.current_journey.pop()
        self.visited_set.remove(node)
    
    def get_all_journeys(self):
        return self.journey_log

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    tracker = PathTracker(graph)
    tracker.explore_with_tracking('A')
    print(f"Total journeys logged: {len(tracker.get_all_journeys())}")
