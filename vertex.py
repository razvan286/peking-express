class Vertex:
    def __init__(self, node, isCritical):
        self.id = node
        # Connections to other nodes
        self.adjacent = {}
        # Mark all nodes unvisited
        self.visited = False
        # Mark the node as critical or non-critical
        self.critial = isCritical

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):  # Returns the neighbors of the vertex
        return self.adjacent.keys()

    def get_id(self):   # Returns the name of the vertex
        return self.id

    def get_weight(self, neighbor):  # Returns the cost of moving from the vertex to its neighbor
        return self.adjacent[neighbor]

    def set_visited(self, value):
        self.visited = value

    def get_visited(self):
        return self.visited
