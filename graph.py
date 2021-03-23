from vertex import *
import copy


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.paths = []
        self.occupiedLocations = []

    def add_vertex(self, node, isCritical):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node, isCritical)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def getAllPathsUtil(self, source, destination, path):

        # Mark the current node as visited and store in path
        source.set_visited(True)
        path.append(source.id)

        # If current vertex is same as destination, then print
        # current path[]
        if source.get_id() == destination.get_id():
           # print(path)
            self.paths.append(copy.deepcopy(path))

        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for neighbor in source.get_connections():
                if neighbor.get_visited() == False:
                    self.getAllPathsUtil(
                        neighbor, destination, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        source.set_visited(False)

    def getAllPaths(self, s, d):
        source = self.get_vertex(s)
        destination = self.get_vertex(d)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.getAllPathsUtil(source, destination, path)

    def getPathCost(self, path):
        cost = 0
        # Base case
        if len(path) == 2:
            return self.get_vertex(path[0]).get_weight(self.get_vertex(path[1]))

        # Add up cost of each edge until destination
        for i in range(0, len(path) - 1):
            cost += self.get_vertex(path[i]
                                    ).get_weight(self.get_vertex(path[i+1]))
        return cost

    def getPekingPath(self, source, destination, cost):
        self.getAllPaths(source, destination)
        self.paths.sort(key=len)
        shortestPathInBudget = []
        for path in self.paths:
            if self.getPathCost(path) <= cost:
                shortestPathInBudget = path
                break
        finalPath = []
        # Add the first move, which is always allowed
        for i in range(2):
            finalPath.append(shortestPathInBudget[0])
            shortestPathInBudget.pop(0)

        while shortestPathInBudget:
            # If the node that you are trying to move to is not critical, or if it's not in the occupied list
            if (self.get_vertex(shortestPathInBudget[0]).critial == False) or (not self.occupiedLocations) or (shortestPathInBudget[0] not in self.occupiedLocations[0]):
                # Move to node, add it to finalPath and remove from temporary
                finalPath.append(shortestPathInBudget[0])
                shortestPathInBudget.pop(0)
            # If the node that you are trying to move to is a critical node that is busy
            else:
                # Wait a turn
                finalPath.append(finalPath[-1])
            # Removes the occupied locations for the day, guarded by an if in order not to pop from an empty list
            if (self.occupiedLocations):
                self.occupiedLocations.pop(0)
        return finalPath
