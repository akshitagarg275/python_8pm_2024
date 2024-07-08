'''
asyncio library helps us in achieving concurrent programming
'''

import asyncio

async def func():
    print("Inside the function")
    await asyncio.sleep(1)
    print("Asynchronous Programming")
    await asyncio.sleep(1)
    print("It is not multi threading")

# asyncio.run(func())

# TODO: async event loop
async def f1():
    print("one")
    await asyncio.sleep(1)
    await f2()
    print("four")
    await asyncio.sleep(1)
    print("five")
    await asyncio.sleep(1)

async def f2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")

# asyncio.run(f1())

# TODO: Actual Asynchronous Programming

async def fn():
    task1=asyncio.create_task(fn2())
    print('One')
    print('Four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)

async def fn2():
    print('two')
    await asyncio.sleep(1)
    print('three')

# asyncio.run(fn())

# TODO: I/O bound tasks

async def func1():
    print("Function 1 started...")
    await asyncio.sleep(2)
    print("Function 1 ended")

async def func2():
    print("Function 2 started...")
    await asyncio.sleep(2)
    print("Function 2 ended")

async def func3():
    print("Function 3 started...")
    await asyncio.sleep(2)
    print("Function 3 ended")


async def main():
    var = await asyncio.gather(func1(), func2(), func3())

    print("main ended")

asyncio.run(main())


