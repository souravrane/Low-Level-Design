from customThreadPool import CustomThreadPool
from numberPrinter import NumberPrinter

if __name__ == "__main__":
    # If you want to turn the thread pool into cached thread pool, use max_workers = None
    threadPool = CustomThreadPool(5)
    for i in range(100):
        task = NumberPrinter(i)
        threadPool.submit(task)
    
    threadPool.shutdown()
    print("All tasks completed")