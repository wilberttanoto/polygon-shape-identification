class CycleGraph(object):
    def __init__(self, graph):
        self.graph = graph
        self.cycles = []

    def getAllCyclyes(self):
        for edge in self.graph:
            for node in edge:
                self.findCycles([node])
        
        return self.cycles
        
    def findCycles(self, path):
        start_node = path[0]
        next_node= None
        sub = []

        # visit each edge and each node of each edge
        for edge in self.graph:
            node1, node2 = edge
            if start_node in edge:
                if node1 == start_node:
                    next_node = node2
                else:
                    next_node = node1
                if not self.visited(next_node, path):
                    # neighbor node not on path yet
                    sub = [next_node]
                    sub.extend(path)
                    # explore extended path
                    self.findCycles(sub);
                elif len(path) > 2 and next_node == path[-1]:
                    # cycle found
                    p = self.rotateToSmallest(path);
                    inv = self.invert(p)
                    if self.isNew(p) and self.isNew(inv):
                        self.cycles.append(p)

    def invert(self, path):
        return self.rotateToSmallest(path[::-1]) # all items in the array, reversed

    # rotate cycle path such that it begins with the smallest node
    def rotateToSmallest(self, path):
        n = path.index(min(path))
        return path[n:]+path[:n]

    def isNew(self, path):
        return not path in self.cycles

    def visited(self, node, path):
        return node in path

    