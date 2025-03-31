<!-- BFS vs DFS -->

Breadth First Search: 
- Start with iterating through levels of a tree, then proceeds to go to the next deeper level.
- usually uses more memory because it stores all nodes, whereas DFS will only store one path of node at a time. 
- faster for wider graphs
- useful for finding the shortest path, or when answers are found frequently

DFS: 
- Start with iterating through one path, the moves on to the next level
- uses less memory than BFS vice versa
- faster for deeper graphs
- useful for finding whether a path exists for two nodes. 