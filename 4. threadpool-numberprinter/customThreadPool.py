from concurrent.futures import ThreadPoolExecutor

class CustomThreadPool:
    def __init__(self, max_workers: int):
        self.executor = ThreadPoolExecutor(max_workers = max_workers)
    
    def submit(self, task):
        self.executor.submit(task.execute)
    
    def shutdown(self):
        self.executor.shutdown(wait = True)