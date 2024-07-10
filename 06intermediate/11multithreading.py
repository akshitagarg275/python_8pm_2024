'''
Multithreading

thread: it is a sequence of instructions within a program that can be
        executed independently of other code

Thread Control Block (TCB):
- Thread Identifier
= Stack Pointer
= Program Counter
= Thread State
= Thread Register
- Parent Process Pointer

GIL -> Global interpreter Lock , it limits the execution of only one thread at a time
for CPU bound tasks
'''
import threading

def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")