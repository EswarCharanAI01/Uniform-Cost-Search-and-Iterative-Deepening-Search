import heapq


class PriorityQueue:
    # Constructor for initializing a Priority Queue
    def __init__(self):
        self.heap = []

    # Inserting a new key 'key'
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    # function to remove the element that is minimum, from the Priority Queue
    def pop(self):
        return heapq.heappop(self.heap)[1]

    # function to check if the PriorityQueue is empty or not
    def empty(self):
        if not self.heap:
            return True
        else:
            return False
