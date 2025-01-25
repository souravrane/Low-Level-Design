class Node:
    def __init__(self, data: int, next: 'Node' = None):
        self.data = data
        self.next = next

    def __iter__(self):
        current = self
        while current:
            yield current.data # Return the data of the current node
            current = current.next