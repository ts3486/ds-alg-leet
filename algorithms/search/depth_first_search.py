def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Track visited nodes
    
    print(start, end=' ')  # Process the node
    visited.add(start)  # Mark as visited
    
    for neighbor in graph.get(start, []):  # Explore neighbors
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursive DFS call

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS Traversal:")
dfs(graph, 'A')

#pre-order, in-order, post-order

# Pre-Order (NLR)	Node → Left → Right	Copying a tree, prefix notation
# In-Order (LNR)	Left → Node → Right	Sorting BSTs
# Post-Order (LRN)	Left → Right → Node	Deleting trees, postfix notation