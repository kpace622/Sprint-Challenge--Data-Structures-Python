class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.storage = []

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else: 
            for x in self.storage:
                current = 0
                self.storage[current] = item
                current = current + 1

    def get(self):
        return self.storage
