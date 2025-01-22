from customThreadPool import CustomThreadPool
from computeSquare import ComputeSquareTask

if __name__ == "__main__":
    threadPool = CustomThreadPool()
    futures = list()

    for i in range(1,20):
        task = ComputeSquareTask(i)
        future = threadPool.submit_task(task)
        futures.append(future)
    
    result = [fut.result() for fut in futures]
    print("Squares computed : ", result)

    threadPool.shutdown()
    print("All tasks completed.")
