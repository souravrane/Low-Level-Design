from threading import Thread 
from task import Task

class ThreadWorker(Thread):
    def __init__(self, task: Task, name: str = None):
        super().__init__(name = name)
        self.task = task

    def run(self):
        self.task.execute()


