# Creating a class to keep grid and its relevant data
class Node:
    def __init__(self, parent, grid, emptyTile, level):
        self.parent = parent
        self.grid = grid
        self.emptyTile = emptyTile
        self.level = level

    def __lt__(self, other):
        return self.level < other.level
