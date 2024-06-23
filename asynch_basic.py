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
    # get current running event loop
    loop = asyncio.get_running_loop()
    if loop is not None:
        print(f"the current running loop is : {loop}")

    print(f"the current task is :{asyncio.current_task()}")
    print(f"all tasks: {'-->' * 5 } \n ")
    for task in asyncio.all_tasks():
        print(
            f"{'-->' * 6} \n {task.get_name()} \n : done:{task.done()} \n"
            + f"cancelled : {task.cancelled()} \n"
            + f"stack : {task.get_stack()}"
        )

        # 3.12 added get_context()
        # print(f"context: {task.get_context()}")


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def eternity():
    # sleep for one hour
    await asyncio.sleep(3600)
    print("finally after one hour: Yeh!")


def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io finished at {time.strftime('%X')}")


async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main():

    try:

        # limit the amount of time spent waiting on something.
        # if the program under async with part takes more than
        # X seconds to complete, the context manager will cancel
        # the current task and transforming to TimeoutError.
        async with asyncio.timeout(2) as atm:

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

            # awaitable asyncio.shield(aw)
            # Protect an awaitable object from being cancelled.
            # If aw is a coroutine it is automatically scheduled as a Task.
            result = await asyncio.shield(task4)
            print(f"result from task4 is {result}")
            print(f"concurrently finished at {time.strftime('%X')}")

            # The asyncio.TaskGroup class provides a more modern alternative
            # to create_task(). Using this API, the last example becomes
            print(f"Taskgroup started at {time.strftime('%X')}")
    except TimeoutError:
        print("the operation timed out, handled it here")
    except asyncio.CancelledError:
        print("the task was canceled.")
    finally:
        print("here is the clean up part of the program")

    if atm.expired():
        print("Looks like we haven't finished on time!")

    try:

        loop = asyncio.get_running_loop()
        deadline = loop.time() + 2
        async with asyncio.timeout_at(deadline) as ta:
            async with asyncio.TaskGroup() as tg:

                task5 = tg.create_task(say_after(2, "task5 hello!"))
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

        # concurrent tasks by gather.
        # Schedule three calls *concurrently*:
        """
        A new alternative to create and run tasks concurrently and 
        wait for their completion is asyncio.TaskGroup. 
        TaskGroup provides stronger safety guarantees than gather 
        for scheduling a nesting of subtasks: if a task (or a subtask,
        a task scheduled by a task) raises an exception, 
        TaskGroup will, while gather will not, 
        cancel the remaining scheduled tasks).
        """
        L = await asyncio.gather(
            factorial("A", 2),
            factorial("B", 3),
            factorial("C", 4),
        )
        print(L)

    except TimeoutError:
        print("the operation timed out, handled it here")
    except asyncio.CancelledError:
        print("the task was canceled.")
    finally:
        print("here is the clean up part of the program")

    # this statement will run regardless.
    if ta.expired():
        print("Looks like we haven't finished on time!")

    try:
        await asyncio.wait_for(eternity(), timeout=1)
    except TimeoutError:
        print("the wait_for operation timed out, handled it here")

    """
    coroutine asyncio.to_thread(func, /, *args, **kwargs)
    Asynchronously run function func in a separate thread.
    This coroutine function is primarily intended to be used 
    for executing IO-bound functions/methods that 
    would otherwise block the event loop if they were run in the main thread.

    """
    print(f"main started at {time.strftime('%X')}")
    await asyncio.gather(asyncio.to_thread(blocking_io), asyncio.sleep(1))
    print(f"main completed at {time.strftime('%X')}")

    # example of the cancelation request:
    task13 = asyncio.create_task(cancel_me())

    await asyncio.sleep(1)
    task13.cancel()
    try:
        await task13
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now!")

# asyncio.run(main())
# or
with asyncio.Runner() as runner:
    runner.run(main())
