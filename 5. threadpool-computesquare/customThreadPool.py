from concurrent.futures import ThreadPoolExecutor 
from task import Task

class CustomThreadPool:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers = None)

    def submit_task(self, task : Task):
        return self.executor.submit(task.execute)
    
    def shutdown(self):
        self.executor.shutdown(wait = True)
