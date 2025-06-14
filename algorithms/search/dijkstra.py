import heapq
from typing import Dict, List, Set, Tuple

def dijkstra(graph: Dict[str, List[Tuple[str, int]]], start: str) -> Dict[str, int]:
    """
    Implements Dijkstra's algorithm to find shortest paths from a start node to all other nodes.
    
    Args:
        graph: Dictionary representing the graph where each key is a node and value is a list of
              (neighbor, weight) tuples
        start: Starting node for the algorithm
    
    Returns:
        Dictionary mapping each node to its shortest distance from the start node
    """
    # Initialize distances dictionary with infinity for all nodes except start
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue to store (distance, node) pairs
    priority_queue = [(0, start)]
    
    # Set to keep track of visited nodes
    visited: Set[str] = set()
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we've already processed this node, skip it
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        # Check all neighbors of the current node
        for neighbor, weight in graph[current_node]:
            # Calculate new distance to neighbor
            distance = current_distance + weight
            
            # If we found a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list with weights
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    # Find shortest paths from node 'A'
    shortest_paths = dijkstra(graph, 'A')
    
    print("Shortest paths from node A:")
    for node, distance in shortest_paths.items():
        print(f"To {node}: {distance}")
