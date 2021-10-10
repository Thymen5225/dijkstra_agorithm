from collections import defaultdict


# Initializing the Graph Class
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        if toNode in self.nodes:
            self.edges[fromNode].append(toNode)
            self.distances[(fromNode, toNode)] = distance
        else:
            pass


# Implementing Dijkstra's Algorithm
def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]
        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path


def find_path(path, begin, end):
    path_lst = [end]
    calculating = True
    while calculating:
        previous = path[end][0]
        path_lst.append(previous)
        if previous == begin:
            calculating = False
        else:
            end = previous
    return path_lst[::-1]


def create_graph_from_matrix(size, matrix):
    G = Graph()
    for i in range(len(matrix)):
        G.addNode(i)

    hlist_right = []
    hlist_left = []
    for i in range(size):
        hlist_right.append(size * (i + 1) - 1)
        hlist_left.append(size * (i + 1))

    for i in range(len(matrix)):
        if not matrix[i]:
            if i + 1 in G.nodes and not matrix[i + 1] and i not in hlist_right:
                G.addEdge(i, i + 1, 1)
            if i - 1 in G.nodes and not matrix[i - 1] and i not in hlist_left:
                G.addEdge(i, i - 1, 1)
            if i + size in G.nodes and not matrix[i + size]:
                G.addEdge(i, i + size, 1)
            if i - size in G.nodes and not matrix[i - size]:
                G.addEdge(i, i - size, 1)

    return G
