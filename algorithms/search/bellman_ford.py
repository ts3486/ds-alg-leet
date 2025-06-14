from typing import Dict, List, Tuple, Optional

def bellman_ford(graph: Dict[str, List[Tuple[str, int]]], start: str) -> Optional[Dict[str, int]]:
    """
    Implements Bellman-Ford algorithm to find shortest paths from a start node to all other nodes.
    Can detect negative cycles in the graph.
    
    Args:
        graph: Dictionary representing the graph where each key is a node and value is a list of
              (neighbor, weight) tuples
        start: Starting node for the algorithm
    
    Returns:
        Dictionary mapping each node to its shortest distance from the start node,
        or None if a negative cycle is detected
    """
    # Initialize distances dictionary with infinity for all nodes except start
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Get all edges in the graph
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((node, neighbor, weight))
    
    # Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u, v, w in edges:
            if distances[u] != float('infinity') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    
    # Check for negative cycles
    for u, v, w in edges:
        if distances[u] != float('infinity') and distances[u] + w < distances[v]:
            print("Negative cycle detected!")
            return None
    
    return distances

# Example usage
if __name__ == "__main__":
    # Example graph with no negative cycles
    graph1 = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    # Example graph with negative cycle
    graph2 = {
        'A': [('B', 1)],
        'B': [('C', 2)],
        'C': [('D', 3)],
        'D': [('B', -6)]  # This creates a negative cycle
    }
    
    print("Testing graph without negative cycles:")
    shortest_paths = bellman_ford(graph1, 'A')
    if shortest_paths:
        for node, distance in shortest_paths.items():
            print(f"To {node}: {distance}")
    
    print("\nTesting graph with negative cycle:")
    shortest_paths = bellman_ford(graph2, 'A')
    if shortest_paths:
        for node, distance in shortest_paths.items():
            print(f"To {node}: {distance}")
