import IDS
import NodeStructure
import UCS

import util

if __name__ == '__main__':
    # grid, randomRow, randomCol = util.generateRandomGrid()
    # start = NodeStructure.Node(None, grid, [randomRow, randomCol], 1)
    start = NodeStructure.Node(None, [[2, 5, 3],[4, 8, 1],[7, 0, 6]], [1, 1], 0)  # - 1st case
    # start = NodeStructure.Node(None, [[5, 3, 8], [0, 2, 7], [6, 4, 1]], [1, 0], 1)  # - 2nd case
    # start = NodeStructure.Node(None, [[8, 4, 6], [3, 2, 5], [7, 1, 0]], [2, 2], 1)  # - 3nd case
    # start = NodeStructure.Node(None, [[6, 7, 2],[0, 5, 3],[8, 4, 1]], [1, 0],1) # - 4th case

    # print("Initial Grid Configuration-")
    # for configGrid in grid:
    #     print(configGrid)
    print("Goal Grid Configuration-")
    for goalRow in util.goal:
        print(goalRow)

    solved, noOfNodesChecked, totalTime, UCSNodesVisited, level = UCS.UCS(start)
    print("Able to find solution using UCS - ", solved)
    print("Number Of Nodes visited - ", noOfNodesChecked, "Total Time Taken - ", totalTime)
    solutionFound, maxHeight, allNodesVisited, allNumberOfNodesChecked, totalTime, noOfNodesChecked = IDS.IDS(start)
    print("Able to find solution using IDS - ", solutionFound)
    print("Number Of Nodes visited - ", allNumberOfNodesChecked, "Total Time Taken - ", totalTime)
    print("Number of nodes checked at last depth - ", noOfNodesChecked)
