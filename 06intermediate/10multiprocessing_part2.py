import multiprocessing
import os

def worker1():
    print(f"Id of process running worker 1: {os.getpid()}")

def worker2():
    print(f"Id of process running worker 2: {os.getpid()}")

if __name__ == '__main__':
    print(f"Id of main process: {os.getpid()}")

    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    p1.start()
    p2.start()

    print(f"Id of process p1: {p1.pid}")
    print(f"Id of process p1: {p2.pid}")

    p1.join()
    p2.join()

    print("Both processes completed!")

    print(f"Is P1 process alive: {p1.is_alive()}")
    print(f"Is P2 process alive: {p2.is_alive()}")

