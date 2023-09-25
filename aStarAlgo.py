def aStarAlgo(source, destination):
    # initial-config
    openSet = set(source)
    closedSet = set()
    dist = {}
    parent = {}

    dist[source] = 0
    parent[source] = source
    
    while len(openSet) > 0 :
        curNode = None

        # find the node with the least distance from the source
        for node in openSet:
            if curNode == None or dist[node] + heuristicDist[node] < dist[curNode] + heuristicDist[curNode] :
                curNode = node

        # if we have reached the end, construct the path and stop
        if curNode == destination:
            path = []
            while parent[curNode] != curNode:
                path.append(curNode)
                curNode = parent[curNode]
            path.append(curNode)
            path.reverse()
            print("Path found: {}".format(path))
            return
        
        # exploring the neighbors of the current node similar to dijkstra's algorithm
        for (neighbor, weight) in adj[curNode] :
            if neighbor not in openSet and neighbor not in closedSet :
                parent[neighbor] = curNode
                dist[neighbor] = dist[curNode] + weight
                openSet.add(neighbor)
            elif dist[neighbor] > dist[curNode] + weight :
                parent[neighbor] = curNode
                dist[neighbor] = dist[curNode] + weight
                if neighbor in closedSet:
                    closedSet.remove(neighbor)
                    openSet.add(neighbor)
        
        # we have explored all the neighbors of the current node
        openSet.remove(curNode)
        closedSet.add(curNode)
    
    # if we reached here, then there is no path from the given source to the destination
    print("Path--- doesn't exist")
    return

heuristicDist = {
    'A' : 10,
    'B' : 8,
    'C' : 5,
    'D' : 7,
    'E' : 3,
    'F' : 6,
    'G' : 5,
    'H' : 3,
    'I' : 1,
    'J' : 0
}
adj = {
    'A' : [('B', 6), ('F', 3)],
    'B' : [('C', 3), ('D', 2)],
    'C' : [('D', 1), ('E', 5)],
    'D' : [('C', 1), ('E', 8)],
    'E' : [('I', 5), ('J', 5)],
    'F' : [('G', 1), ('H', 7)],
    'G' : [('I', 3)],
    'H' : [('I', 2)],
    'I' : [('E', 5), ('J', 3)]
}
aStarAlgo('A' , 'J') # AIML version of Dijkstra's (SSSP) algorithm with heuristic distances