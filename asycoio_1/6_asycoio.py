# example of waiting for a coroutine with a timeout
from random import random
import asyncio
import time

# coroutine to execute in a new task
async def task_coro (arg):
    # generate a random value between 0 and 1 
    value = 1 + random()
    # report message
    print(f'{time.ctime()} >task got {value}')
    # block for a moment
    await asyncio.sleep(value)
    # report all tome
    print (f'{time.ctime()} >task done')

# main coroutine
async def main():
    # create a task
    task = task_coro(1)
    #execute and wait for the task without a timeout
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio. TimeoutError:
        print (f'{time. ctime()} Gave up waiting, task canceled')
        
# start the asyncio program
asyncio.run(main())


##Answer
# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/I9Wed Jul 12 15:10:06 2023 >task got 1.8122216516040326        
# Wed Jul 12 15:10:07 2023 Gave up waiting, task canceled      
# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IWed Jul 12 15:10:12 2023 >task got 1.3280663798773762        
# Wed Jul 12 15:10:12 2023 Gave up waiting, task canceled      
# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/asycoio_1/6_asycoio.py
# Wed Jul 12 15:10:15 2023 >task got 1.1916965669632649        
# Wed Jul 12 15:10:15 2023 Gave up waiting, task canceled      
# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/asycoio_1/6_asycoio.py
# Wed Jul 12 15:10:17 2023 >task got 1.7000592306251248        
# Wed Jul 12 15:10:17 2023 Gave up waiting, task canceled      
# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/asycoio_1/6_asycoio.py
# Wed Jul 12 15:10:18 2023 >task got 1.348911244916851
# Wed Jul 12 15:10:19 2023 Gave up waiting, task canceled