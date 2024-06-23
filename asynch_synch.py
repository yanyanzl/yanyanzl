"""
asyncio synchronization primitives are designed to be similar
 to those of the threading module with two important caveats:

    asyncio primitives are not thread-safe, therefore they 
    should not be used for OS thread synchronization (use threading for that);

    methods of these synchronization primitives do not accept the 
    timeout argument; use the asyncio.wait_for() function to 
    perform operations with timeouts.

"""
import asyncio


async def syn_lock():
    """
    Implements a mutex lock for asyncio tasks. Not thread-safe.

    An asyncio lock can be used to guarantee exclusive access 
    to a shared resource.

    The preferred way to use a Lock is an async with statement:
    """
    lock = asyncio.Lock()
    x = 0
    # ... later
    async with lock:
        # access shared state
        x = 1000 * 1000
        return x


async def waiter(event):
    """
    An event object. Not thread-safe.
    An asyncio event can be used to notify multiple asyncio tasks
    that some event has happened.
    An Event object manages an internal flag that can be set to
    true with the set() method and reset to false 
    with the clear() method. The wait() method blocks until 
    the flag is set to true. The flag is set to false initially.
    """
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

"""
Semaphore
    A Semaphore object. Not thread-safe.

    A semaphore manages an internal counter which is decremented 
    by each acquire() call and incremented by each release() call.
    The counter can never go below zero; when acquire() finds 
    that it is zero, it blocks, waiting until some task calls release().

    The optional value argument gives the initial value for the 
    internal counter (1 by default). If the given value is 
    less than 0 a ValueError is raised.

"""

"""
    Barrier
    class asyncio.Barrier(parties)
    A barrier object. Not thread-safe.
    A barrier is a simple synchronization primitive that allows 
    to block until parties number of tasks are waiting on it. 
    Tasks can wait on the wait() method and would be blocked
      until the specified number of tasks end up waiting on 
      wait(). At that point all of the waiting tasks would 
      unblock simultaneously.

    async with can be used as an alternative to awaiting on wait().
    The barrier can be reused any number of times.
"""


async def example_barrier():
    # barrier with 3 parties
    b = asyncio.Barrier(3)

    # create 2 new waiting tasks
    asyncio.create_task(b.wait())
    asyncio.create_task(b.wait())

    await asyncio.sleep(0)
    print(b)

    # The third .wait() call passes the barrier
    await b.wait()
    print(b)
    print("barrier passed")

    await asyncio.sleep(0)
    print(b)


async def main():
    x = 10
    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event.
    await asyncio.sleep(1)
    event.set()
    print("event.set done...")

    # Wait until the waiter task is finished.
    await waiter_task

    # ***** semaphore example
    sem = asyncio.Semaphore(10)

    # ... later
    async with sem:
        # work with shared resource
        x += 1
        print(f"now i am in semaphore. Locked? : {sem.locked()}")
        await example_barrier()
    




asyncio.run(main())