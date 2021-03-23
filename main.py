import json
import ast
from graph import Graph


def getUniqueVertixes(source, target):
    uniqueVertex = []
    for i in source:
        if i not in uniqueVertex:
            uniqueVertex.append(i)
    for x in target:
        if x not in uniqueVertex:
            uniqueVertex.append(x)
    return uniqueVertex


def getPath(mapPath, graph):
    # Holds the contents of the text file
    allText = []
    # read the text file and assign to variables
    file = open(mapPath)
    for line in file:
        allText.append(line.strip())

    # assign the variables
    jsonMap = json.loads(allText[0])
    startLocation = int(allText[1])
    budget = int(allText[2])
    occupiedLocations = allText[3]
    graph.occupiedLocations = ast.literal_eval(occupiedLocations)
    source = jsonMap['connections']['source']
    target = jsonMap['connections']['target']
    price = jsonMap['connections']['price']
    criticalLocations = jsonMap['locations']['critical']

    uniqueVertixes = []
    # get the unique vertixes to create the graph
    uniqueVertixes = getUniqueVertixes(source, target)
    for vertex in uniqueVertixes:
        if vertex in criticalLocations:
            graph.add_vertex(vertex, True)
        else:
            graph.add_vertex(vertex, False)

    # add all edges
    for i in range(0, len(source)):
        graph.add_edge(source[i], target[i], price[i])

    print(graph.getPekingPath(startLocation, 88, budget))


if __name__ == '__main__':
    g = Graph()
    getPath("test1.txt", g)
