from task import Task
import threading

class ComputeSquareTask(Task):
    def __init__(self, number : int):
        self.number = number
    
    def execute(self):
        threadName = threading.current_thread().name
        result = self.number * self.number
        print((f"Thread-{threadName} computed square: {self.number}^2 = {result}"))
        return result