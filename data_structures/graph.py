# # Edge List
# graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# # Adjacent List
# graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

# # Adjacent Matrix
# graph = [
#     [0, 0, 1, 0],[0, 1, 0, 1],[0, 0, 1, 0]
# ]

# graph = {
#     0: [0, 0, 1, 0],
#     1: [0, 1, 0, 1],
#     2: [0, 0, 1, 0]
# }

class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}
        
    def addVertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1
        
    def addEdge(self, node1, node2):
        #undirected Graph
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)
        
    def showConnections(self):
        allNodes = self.adjacent_list.keys()
        for node in allNodes:
            nodeConnections = self.adjacent_list[node]
            connections = ""
            for vertex in nodeConnections:
                connections += vertex + ""
            print(node + "-->" + connections)
            
            
myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showConnections()