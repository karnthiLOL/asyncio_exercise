# example of using asyncio shield to protect a task from cancellation 
import time
import asyncio
# define a simple asynchronous 
async def simple_task(number):
    # block for a moment 
    await asyncio.sleep(1)
    # return the argument
    return number

# cancel the given task after a moment 
async def cancel_task(task):
    # block for a moment 
    await asyncio.sleep(0.2)
    # cancel the task
    was_canceled =  task.cancel()
    print(f'{time.ctime()} canceled: {was_canceled}')

# define a simple corotine
async def main():
    # create the coroutine
    coro = simple_task(1)
    # create a task
    task = asyncio.create_task(coro)
    # create the shielded task
    shielded = asyncio.shield(task)
    # create the task to cancel the previous task 
    asyncio.create_task (cancel_task(shielded))
# handle cancellation
    try:    
        # await the shielded task
        result = await shielded
        print(f'{time.ctime()} >got: {result}')
    except asyncio.CancelledError:
        print (f'{time.ctime()} shielded was cancel')
    # wait a moment
    await asyncio.sleep(1)
    # report the details of the tasks
    print (f'{time.ctime()} shielded: {shielded}')
    print (f'{time. ctime()} task: {task}')
    
# start the loop
asyncio.run(main())


##Result
# asyncio.create_task (cancel_task(shielded))
# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/asycoio_1/7_asycoio.py
# Wed Jul 12 15:25:47 2023 canceled: True
# Wed Jul 12 15:25:47 2023 shielded was cancel
# Wed Jul 12 15:25:48 2023 shielded: <Future cancelled>      
# Wed Jul 12 15:25:48 2023 task: <Task finished name='Task-2' coro=<simpl coro=<simple_task() done, defined at e:\00Lab\IOT\asyncio_coio_1\7_asyexercise\asycoio_1\7_asycoio.py:5> result=1>

# asyncio.create_task (cancel_task(task))
# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Lot/AppData/Local/Programs/Python/Python310/python.exe e:/00Lio_exercise/ab/IOT/asyncio_exercise/asycoio_1/7_asycoio.py
# Wed Jul 12 15:26:11 2023 canceled: True
# Wed Jul 12 15:26:11 2023 shielded was cancel
# Wed Jul 12 15:26:12 2023 shielded: <Future cancelled>      
# Wed Jul 12 15:26:12 2023 task: <Task cancelled name='Task-2' coro=<simp' coro=<simple_task() done, defined at e:\00Lab\IOT\asyncioycoio_1\7_as_exercise\asycoio_1\7_asycoio.py:5>>

