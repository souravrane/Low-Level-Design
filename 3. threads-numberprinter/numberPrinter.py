from task import Task
import threading
import time

class NumberPrinter(Task):
    def __init__(self, number:int):
        self.number = number
    
    def execute(self):
        print("printing number", self.number)
        
    