"""
This is the document to learn all about asynchio
Steven 2024-06

asyncio is a library to write concurrent code using the async/await syntax.

asyncio is used as a foundation for multiple Python asynchronous frameworks 
that provide high-performance network and web-servers, database 
connection libraries, distributed task queues, etc.

asyncio is often a perfect fit for IO-bound and high-level 
structured network code.
"""

import asyncio
import time


async def do_something():
    # loop = asyncio.Runner.get_loop(self)
    # await asyncio.sleep(2, print("world!"))
    # print(f"loop is : {loop}")
    x = 0
    for i in range(10000):
        x += i**2
    print(f"x is {x}")


async def say_after(delay, whattosay):
    await asyncio.sleep(delay)
    print(whattosay)


async def current_task():
    print(asyncio.current_task())


async def main():
    print(f"started at {time.strftime('%X')}")

    # will sleep for 1 seconds which finished the first await
    # then start to execute next await which is do_something();
    # so then run sequencely.
    await asyncio.sleep(1, print("hello"))
    await do_something()

    print(f"finished at {time.strftime('%X')}")


    # The asyncio.create_task() function to run coroutines concurrently
    # as asyncio Tasks.
    print(f"concurrently started at {time.strftime('%X')}")
    task1 = asyncio.create_task(say_after(1, "task1 hello!"))
    task2 = asyncio.create_task(do_something())
    task3 = asyncio.create_task(say_after(1, "task3 hello"))
    task4 = asyncio.create_task(current_task())

    await task1
    await task2
    await task3
    await task4
    print(f"concurrently finished at {time.strftime('%X')}")


    # The asyncio.TaskGroup class provides a more modern alternative 
    # to create_task(). Using this API, the last example becomes
    print(f"Taskgroup started at {time.strftime('%X')}")

    async with asyncio.TaskGroup() as tg:
        
        task5 = tg.create_task(say_after(1, "task5 hello!"))
        task6 = tg.create_task(do_something())
        task7 = tg.create_task(say_after(1, "task7 hello"))
        task8 = tg.create_task(current_task())

    print(f"Taskgroup finished at {time.strftime('%X')}")


    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    current_task()

    print(await current_task())

    """
    Save a reference to the result of this function, 
    to avoid a task disappearing mid-execution. 
    The event loop only keeps weak references to tasks. 
    A task that isn’t referenced elsewhere may get garbage collected
    at any time, even before it’s done. For reliable “fire-and-forget”
    background tasks, gather them in a collection:

    """
    background_tasks = set()
    print(f"background_tasks started at {time.strftime('%X')}")

    async with asyncio.TaskGroup() as tg:
        
        task9 = tg.create_task(say_after(1, "task5 hello!"))
        # Add task to the set. This creates a strong reference.
        background_tasks.add(task9)
        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        task9.add_done_callback(background_tasks.discard)

        task10 = tg.create_task(do_something())
        background_tasks.add(task10)
        task10.add_done_callback(background_tasks.discard)

        task11 = tg.create_task(say_after(1, "task7 hello"))
        background_tasks.add(task11)
        task11.add_done_callback(background_tasks.discard)

        task12 = tg.create_task(current_task())
        background_tasks.add(task12)
        task12.add_done_callback(background_tasks.discard)

    print(f"background_tasks finished at {time.strftime('%X')}")


# asyncio.run(main())
# or
with asyncio.Runner() as runner:
    runner.run(main())
