# example of an asynchronous context manager via async with
import asyncio
import time

import asyncio
# define an asynchronous context manager
class AsyncContextManager:
    # enter the async context manager 
    async def __aenter__(self):
        # report a message
        print(f'{time. ctime()}>entering the context manager') 
        # block for a moment
        await asyncio.sleep(0.5)

    # exit the async context manager
    async def __aexit__(self, exc_type, exc, tb):
    # report a message
        print (f'{time. ctime()} >exiting the context manager') 
    # block for a moment 
        await asyncio.sleep(0.5)

# define a simple coroutine 
async def custom_coroutine():
    # create and use the asynchronous context manager 
    async with AsyncContextManager() as manager:
    # report the result
        print (f'{time. ctime()} within the manager')

# start the asyncio program
asyncio.run(custom_coroutine())



## Ans

# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/asycoio_1/10_asycoio.py
# Wed Jul 19 14:11:07 2023>entering the context manager
# Wed Jul 19 14:11:07 2023 within the manager
# Wed Jul 19 14:11:07 2023 >exiting the context manager