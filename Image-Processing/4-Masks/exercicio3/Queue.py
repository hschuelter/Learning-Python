class Queue:

    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len()

    def first(self):
        return self.items[0]

    def printQueue(self):
        print self.items
