# example of getting the current task from the main corotine
import asyncio
#import time to make time_stamp
import time

#define a main corotine
async def main():
    #print time and start_massage
    print(f'(time.ctime()) main corotine started')
    #report a message (old)
    #print('main corotine started')
    #get the current task
    task = asyncio.current_task()
    #print time and task
    print(f'{time.ctime()} {task}')

#start the asyncio program
asyncio.run(main())

##Result
# Wed Jul 12 14:23:58 2023 
# <Task pending name='Task-1' coro=<main() running at e:\00Lab\IOT\asyncio_exercise\asycoio_1\2_asycoio.py:15> 
# cb=[_run_until_complete_cb() at C:\Users\karnt\AppData\Local\Programs\Python\Python310\lib\asyncio\base_events.py:184]>