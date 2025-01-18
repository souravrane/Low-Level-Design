from task import Task
import threading

class NumberPrinter(Task):
    def __init__(self, number: int):
        self.number = number
    
    def execute(self):
        print("Printing ",self.number , " from thread ", threading.current_thread().name)