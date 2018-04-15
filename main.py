#import system arguments
import sys

#read variabls passed from bash shell
try:
    dataDIR = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]
except:
    dataDIR = 'mapping-coding--graph.dat'
    start = 1
    end = 1
    print('Incorrect arguments please make sure to pass <Data source> <From> <To>')

#readFile is a function that read data from file and return an array of strings
#If there is an error in finding the path or reading the file the function will
# throug an error msg
#input: path -> path is a string that refere to the file path
def readFile(path):
    try:
        with open(path) as inputData:
            contents = inputData.read().splitlines()
            inputData.close()
            return contents
    except:
        print("File not found!")

#parseData is a function that split the two lists from the file and return two
#arrays vertices & edges. Vertices contain all the ids and Edges contain all the
#edges info <from> <To> <Distance>
#If there is an error in parsing the data the function will throug an error msg
#input: data -> data is an array of strings that resolt from the readFile
#founction
def parseData(data):
    try:
        vertices = []
        edges = []
        data = map(lambda x: x.split(), data)
        for element in data:
            if len(element)==1:
                vertices.append(element[0])
            else:
                element[2] = int(element[2])
                edges.append(element)
        return vertices, edges
    except:
        print("Parsing data failed!")

#cleanEdges is a function that check if there are negative values in the
# distances, if there is it'll be removed from the list.
#If there is an error in cleaning the data the function will throug an error msg
#input: edges -> edges is an array of all edges.
def cleanEdges(edges):
    try:
        positiveEdges = filter(lambda x : x[2] >= 0 , edges)
        return positiveEdges
    except:
        print("Cleaning data failed!")

#dictionary is a function that compine vertices and edges in one dictionary
#input: vertices & edges -> vertices & edges are lists.
def dictionary(vertices, edges):
    try:
        d = dict.fromkeys(vertices, {})
        for x in edges:
            d[x[0]] = {}
            d[x[1]] = {}
        for x in edges:
            d[x[0]][x[1]] = x[2]
            d[x[1]][x[0]] = x[2]
        return d
    except:
        print("Creating dictionary failed!")

#getShortestPath is the function that calculate the shortest path based on
#Dijkstra algorithm
#input: graph -> is a nested dict that inclue vertices as keys for the first
# dict and the edges and distsnce for the seconed dict
#input: start -> is thae start vetic
#input: end -> is thae end vetic
def getShortestPath(graph, start, end):
    shortestDistance  = {}
    predecessor = {}
    unseenNodes = graph
    infinity = float("inf")
    path = []

    #check if start and end are valied in graph
    if start and end in graph:
        # set initial values for nodes, 0 for start and infinity for else
        for node in unseenNodes:
            shortestDistance[node] = infinity
        shortestDistance[start] = 0

        # calcuslate the min distsnce for paths
        while unseenNodes:
            minNode = None
            for node in unseenNodes:
                if minNode is None:
                    minNode = node
                elif shortestDistance[node] < shortestDistance[minNode]:
                    minNode = node

            for childNode, weight in graph[minNode].items():
                if weight + shortestDistance[minNode] < shortestDistance[childNode]:
                    shortestDistance[childNode] = weight + shortestDistance[minNode]
                    predecessor[childNode] = minNode
            unseenNodes.pop(minNode)
        # find the path nodes
        currentNode = end
        while currentNode != start:
            try:
                path.insert(0,currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print('Path not reachable!')
                break
        path.insert(0,start)
        if shortestDistance[end] != infinity:
            return str(shortestDistance[end])
    else:
        print('Start or end is not valied nodes!')

# command sequence to run the script
try:
    dataString = readFile(dataDIR)
    vertices, edges = parseData(dataString)
    edgesClean = cleanEdges(edges)
    graph = dictionary(vertices, edgesClean)
    result = getShortestPath(graph, start, end)
    print (result + 'm')
except:
    print('Fatal error!')
