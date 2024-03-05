import util
import time
from collections import deque


def IDS(start):
    depth = 0
    # Below maxHeight is used to figure if we are at last level or we can go even further
    maxHeight = 0
    startTime = time.time()
    allNodesVisited = []
    allNumberOfNodesChecked = 0
    # while depth <= 40:
    while depth <= 40:
        depth = depth + 1
        solutionFound, maxHeight, noOfNodesChecked, allNodesVisited = IDS_searchTree(start, depth)
        allNumberOfNodesChecked = allNumberOfNodesChecked + noOfNodesChecked
        if solutionFound == "YES":
            totalTime = time.time() - startTime
            return solutionFound, maxHeight, allNodesVisited, allNumberOfNodesChecked, totalTime, noOfNodesChecked
    return "NO", maxHeight, allNodesVisited, allNumberOfNodesChecked, (time.time() - startTime), None


def IDS_searchTree(startState, depth):
    allNodesVisited = []
    exploredDFS = {}
    noOfNodesChecked = 0
    frontier = deque()  # Maintaining Stack to Implement DFS
    frontier.append(startState)
    maxHeight = 0
    while frontier:
        noOfNodesChecked = noOfNodesChecked + 1  # Counting number of steps
        currentNode = frontier.pop()  # Use pop() for LIFO
        # print("maxHeight", maxHeight, "currentNode.level", currentNode.level)
        maxHeight = max(maxHeight, currentNode.level)
        allNodesVisited.append(currentNode.grid)  # Adding all grid to print
        if util.isGoalState(currentNode.grid):  # checking if goal state reached
            return "YES", maxHeight, noOfNodesChecked, allNodesVisited
        util.findSuccessorIDS(frontier, currentNode, exploredDFS, depth)
    return "NO", maxHeight, noOfNodesChecked, allNodesVisited
