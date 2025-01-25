from adder import Adder
from subtractor import Subtractor
from count import Count
import threading

if __name__ == "__main__":
    count = Count()

    threads = list()
    for _ in range(100):
        t1 = threading.Thread(target = Adder(count, 1).execute)
        t2 = threading.Thread(target = Subtractor(count, 1).execute)
        threads.append(t1)
        threads.append(t2)
    
    for t in threads: t.start()
    for t in threads: t.join()

    print(f"Final count value : {count.getValue()}")