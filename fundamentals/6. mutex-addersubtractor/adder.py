from task import Task

class Adder(Task):
    def __init__(self, count, value):
        self.count = count
        self.value = value
    
    def execute(self):
        self.count.add(self.value)