import multiprocessing

def cube(num):
    print(f"Cube is : {num ** 3}")

def square(num):
    print(f"Square is : {num ** 2}")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=square, args= (10,))
    p2 = multiprocessing.Process(target=cube, args= (10,))

    p1.start()
    p2.start()

    # waits until process 1 is completed
    p1.join()
    # waits until process 2 is completed
    p2.join()

    print("Tasks completed")
