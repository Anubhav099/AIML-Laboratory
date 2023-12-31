class Graph:
    def __init__(self, adj, heuristicValue, sourceNode):
        self.adj = adj
        self.heuristicValue = heuristicValue
        self.sourceNode = sourceNode
        
        self.visited = {}
        self.parent = {}
        self.solutionGraph = {}

    def applyAOStar(self):
        self.aoStar(self.sourceNode, True)

    def getNeighbors(self, curNode):
        return self.adj.get(curNode, [])

    def getVisited(self, curNode):
        return self.visited.get(curNode, False)

    def setVisited(self, curNode, val):
        self.visited[curNode] = val

    def getHeuristicValue(self, curNode):
        return self.heuristicValue.get(curNode, 0)

    def setHeuristicValue(self, curNode, val):
        self.heuristicValue[curNode] = val

        
    def computeMinimumCostChildNodes(self, curNode):
        minCost = 0
        childNodeList = []
        firstTime = True

        for neighTupleList in self.getNeighbors(curNode):
            cost = 0
            nodeList = []
            for (neigh, weight) in neighTupleList:
                cost += self.getHeuristicValue(neigh) + weight
                nodeList.append(neigh)
            if firstTime or cost < minCost:
                minCost = cost
                childNodeList = nodeList
                firstTime = False

        return minCost, childNodeList

    def aoStar(self, curNode, moreRecursiveCalls):
        print("HEURISTIC VALUES:", self.heuristicValue)
        print("SOLUTION GRAPH:", self.solutionGraph)
        print("PROCESSING NODE:", curNode)
        print("---------------")

        if not self.getVisited(curNode):
            minCost, childNodeList = self.computeMinimumCostChildNodes(curNode)
            self.setHeuristicValue(curNode, minCost)
            solved = True
            
        for childNode in childNodeList:
            self.parent[childNode] = curNode
            if not self.getVisited(childNode):
                solved = False

        if solved:
            self.setVisited(curNode, True)
            self.solutionGraph[curNode] = childNodeList

        if curNode != self.sourceNode:
            self.aoStar(self.parent[curNode], False)

        if moreRecursiveCalls:
            for childNode in childNodeList:
                self.setVisited(childNode, False)
                self.aoStar(childNode, True)

    def printSolution(self):
        print('--------------------\nFor solution, traverse the graph from the souce node:', self.sourceNode)
        print("Solution:", self.solutionGraph)
        print("--------------------\n--------------------")

# testing
myHeuristicValue = {'A':1,'B':6,'C':2,'D':12,'E':2,'F':1,'G':5,'H':7,'I':7,'J':1}
myAdj = {
    'A':[[('B',1),('C',1)],[('D',1)]],
    'B':[[('G',1)],[('H',1)]],
    'C':[[('J',1)]],
    'D':[[('E',1),('F',1)]],
    'G':[[('I',1)]]
}
graphObj = Graph(myAdj, myHeuristicValue, 'A')
graphObj.applyAOStar()
graphObj.printSolution()