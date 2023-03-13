from queue import Queue
import time
from threading import Thread


cola = Queue(10)

def productor():
    i = 1
    while True:
        cola.join()
        cola.put(i)
        print(f"Producto {i} colocado en la cola")
        i+=1

def customer():
    i = 1
    while True:
        cola.get()
        print(f"Producto {i} consumido")
        i+=1
        cola.task_done()
        time.sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=productor)
    t2 = Thread(target=customer)
    t1.start()
    t2.start()