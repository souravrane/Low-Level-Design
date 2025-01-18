from numberPrinter import NumberPrinter
from threadWorker import ThreadWorker

if __name__ == "__main__":
    threads = list()

    for i in range(1, 10):
        task = NumberPrinter(i)
        thread = ThreadWorker(task, name = f"Thread-{i}")
        threads.append(thread)

    for thread in threads: thread.start()
    for thread in threads: thread.join()

    print("All threads are done!")    