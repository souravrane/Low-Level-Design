from customThreadPool import CustomThreadPool
from numberPrinter import NumberPrinter

if __name__ == "__main__":
    threadPool = CustomThreadPool(5)
    for i in range(10):
        task = NumberPrinter(i)
        threadPool.submit(task)
    
    threadPool.shutdown()
    print("All tasks completed")