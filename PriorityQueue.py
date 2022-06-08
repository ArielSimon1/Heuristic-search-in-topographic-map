import heapq

# this class is in charge of the priority queue of the nodes in the frontier.
# it helps us to apply the right order of nodes, ad it defindes in the different algorithms.
class PriorityQueue:
    # constructor of the class.
    def __init__(self, f=lambda x: x):
        self.heap = []
        self.f = f
    # this function let us add (append) a node or list of nodes to an object like a frontier.
    def append(self, item):
        heapq.heappush(self.heap, (self.f(item), item))

    # this function uses the "append" function above to append list of objects.
    def extend(self, items):
        for item in items:
            self.append(item)

    # this function takes out (pop) an object (node) from the queue structur.
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    # returns the lenght of a heap object.
    def __len__(self):
        return len(self.heap)

    # returns TRUE if at least one element is true, FALSE otherwise.
    def __contains__(self, key):
        return any([item == key for _, item in self.heap])

    # returns an item or items, if they are in the heap.
    def __getitem__(self, key):
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    # delete item from the queue or heap
    def __delitem__(self, key):
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)

    # returns the string version of the heap
    def __repr__(self):
            return str(self.heap)