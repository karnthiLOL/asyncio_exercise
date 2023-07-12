#example of running a coroutine
import asyncio
#import time to make time_stamp
import time

# define a coroutine
async def custom_coro():
    # wait for a tak to be done
    # await another corotine
    await asyncio.sleep(1)

#main corotine
async def main():
    #execute my custom coroutine
    await custom_coro()
    #print time and start_massage
    print(f'(time.ctime()) main corotine started')
    #print time and task
    print(f'{time.ctime()}')

#Start the coroutine programs
asyncio.run(main())


##Result
# Wed Jul 12 14:26:04 2023