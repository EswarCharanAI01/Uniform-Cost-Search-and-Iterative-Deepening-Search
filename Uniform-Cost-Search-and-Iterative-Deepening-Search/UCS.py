import util
import time
import PriorityQueue


def UCS(startState):
    startTime = time.time()  # keeping counter for starting time
    allNodesVisited = []  # holds all visited nodes
    explored = {tuple(tuple(row) for row in startState.grid): 1}  # holds all nodes for duplicate node check
    noOfNodesChecked = 0  # counts number of nodes visited
    frontier = PriorityQueue.PriorityQueue()  # priority queue, gives elements with lower cost value
    frontier.push(startState, startState.level)
    while not frontier.empty():
        noOfNodesChecked = noOfNodesChecked + 1  # Counting number of steps
        currentNode = frontier.pop()
        allNodesVisited.append(tuple(tuple(row) for row in currentNode.grid))  # Adding all grid to print
        # allNodesVisited.append(currentNode.grid)  # Adding all grid to print
        if util.isGoalState(currentNode.grid):  # checking if goal state reached
            totalTime = time.time() - startTime
            return "YES", noOfNodesChecked, totalTime, allNodesVisited, currentNode.level
        util.findSuccessorUCS(frontier, currentNode, explored)
    totalTime = time.time() - startTime
    return "NO", noOfNodesChecked, totalTime, allNodesVisited, None
