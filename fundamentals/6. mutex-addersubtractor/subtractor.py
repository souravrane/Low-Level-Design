from task import Task

class Subtractor(Task):
    def __init__(self, count, value):
        self.count = count
        self.value = value
    
    def execute(self):
        self.count.subtract(self.value)