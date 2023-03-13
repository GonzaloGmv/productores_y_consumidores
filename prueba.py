from queue import Queue
from threading import Thread
import time

q = Queue(10)

def producer():
    count = 1
    while True:
        q.join()
        q.put(count)
        print(f"El productor está produciendo el {count}")
        count+=1

def customer():
    count = 1
    while True:
        q.get()
        print(f"El consumidor está consumiendo el {count}")
        count+=1
        q.task_done()
        time.sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=producer)
    t2 = Thread(target=customer)
    t1.start()
    t2.start()