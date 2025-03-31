from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize queue with the start node
    
    while queue:
        node = queue.popleft()  # Get the first node in the queue
        
        if node not in visited:
            print(node, end=' ')  # Process the node (e.g., print it)
            visited.add(node)  # Mark as visited
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal:")
bfs(graph, 'A')

from collections import deque

def bfs_recursive(graph, queue, visited):
    if not queue:  # Base case: Stop if the queue is empty
        return
    
    node = queue.popleft()  # Get the first node in the queue
    
    if node not in visited:
        print(node, end=' ')  # Process the node
        visited.add(node)  # Mark as visited
        
        # Add all unvisited neighbors to the queue
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
    
    # Recursive call with updated queue
    bfs_recursive(graph, queue, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recursive BFS Traversal:")
bfs_recursive(graph, deque(['A']), set())