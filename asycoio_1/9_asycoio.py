# example of an asynchronous iterator with async for loop
import asyncio
import time

# define an asynchronous iterator
class AsyncIterator():
    # constructor, define some state
    def __init__(self):
        self.counter = 0

    # create an instance of iterator
    def __aiter__(self):
        return self
    
    # return the next awaitable
    async def __anext__(self):
        # check for no furture items
        if self.counter >= 10:
            raise StopAsyncIteration
        # increment the couter
        self.counter += 1
        # simulate work
        await asyncio.sleep(1)
        # return the couter value
        return self.counter
    
# main coroutine
async def main():
    # loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(f'{time.ctime()} {item}')
# execute the asyncio program
asyncio.run(main())


## Ans

# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/asycoio_1/9_asycoio.py
# Wed Jul 19 13:58:16 2023 1
# Wed Jul 19 13:58:17 2023 2
# Wed Jul 19 13:58:18 2023 3
# Wed Jul 19 13:58:19 2023 4
# Wed Jul 19 13:58:20 2023 5
# Wed Jul 19 13:58:21 2023 6
# Wed Jul 19 13:58:22 2023 7
# Wed Jul 19 13:58:23 2023 8
# Wed Jul 19 13:58:24 2023 9
# Wed Jul 19 13:58:25 2023 10