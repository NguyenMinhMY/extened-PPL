class Graph:
    def __init__(self, liveRanges):
        self.liveRanges = liveRanges
        self.adjList = self.initAdjList()

    def initAdjList(self):
        adjList = {}

        for node in self.liveRanges.keys():
            adjList[node] = []
        
        for u in self.liveRanges.keys():
            for v in self.liveRanges.keys():
                if v != u:
                    if (self.liveRanges[v][1] >= self.liveRanges[u][0]) and (self.liveRanges[u][1] >= self.liveRanges[v][0]):
                        adjList[u].append(v) 

        return adjList


    def neighbors(self, node):
        return self.adjList[node]
    
class Chaitin:
    def __init__(self, graph, k):
        self.graph = graph
        self.k = k

    def color_graph(self):
        color_map = {}

        # Assign initial colors to all nodes
        for node in self.graph.adjList:
            color_map[node] = None

        # Iteratively select nodes to color
        for node in self.graph.adjList:
            available_colors = set(range(self.k))

            # Check the colors of neighboring nodes
            for neighbor in self.graph.adjList[node]:
                if neighbor in color_map:
                    color = color_map[neighbor]
                    if color in available_colors:
                        available_colors.remove(color)

            # Assign the lowest available color to the node
            if len(available_colors) > 0:
                color_map[node] = min(available_colors)
            else:
                color_map[node] = self.k
                self.k += 1

        return color_map