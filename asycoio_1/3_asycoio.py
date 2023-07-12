#example of starting many task and getting access to all task
import asyncio
import time

#coroutine for a task
async def task_corotine(value):
    #report a message
    print(f'{time.ctime()} task {value} is running')
    #block for a moment
    await asyncio.sleep(1)

#define a main corotine
async def main():
    #print time and start_massage
    print(f'{time.ctime()} main corotine started')
    #start many tasks
    start_tasks = [asyncio.create_task(task_corotine(i)) for i in range(20)]
    #allow some of the tasks time to start
    await asyncio.sleep(0.1)
    #get all task
    tasks = asyncio.all_tasks()
    #report all tasks
    for task in tasks:
        print(f'{time.ctime()} > {task.get_name()}, {task.get_coro()}')
    #wait for all task to complete
    for task in start_tasks:
        await task

#start the asycio program
asyncio.run(main())    


##Result
# Wed Jul 12 14:39:11 2023 main corotine started
# Wed Jul 12 14:39:11 2023 task 0 is running
# Wed Jul 12 14:39:11 2023 task 1 is running
# Wed Jul 12 14:39:11 2023 task 2 is running
# Wed Jul 12 14:39:11 2023 task 3 is running
# Wed Jul 12 14:39:11 2023 task 4 is running
# Wed Jul 12 14:39:11 2023 task 5 is running
# Wed Jul 12 14:39:11 2023 task 6 is running
# Wed Jul 12 14:39:11 2023 task 7 is running
# Wed Jul 12 14:39:11 2023 task 8 is running
# Wed Jul 12 14:39:11 2023 task 9 is running
# Wed Jul 12 14:39:11 2023 task 10 is running
# Wed Jul 12 14:39:11 2023 task 11 is running
# Wed Jul 12 14:39:11 2023 task 12 is running
# Wed Jul 12 14:39:11 2023 task 13 is running
# Wed Jul 12 14:39:11 2023 task 14 is running
# Wed Jul 12 14:39:11 2023 task 15 is running
# Wed Jul 12 14:39:11 2023 task 16 is running
# Wed Jul 12 14:39:11 2023 task 17 is running
# Wed Jul 12 14:39:11 2023 task 18 is running
# Wed Jul 12 14:39:11 2023 task 19 is running
# Wed Jul 12 14:39:11 2023 > Task-1, <coroutine object main at 0x000001918E961310>
# Wed Jul 12 14:39:11 2023 > Task-13, <coroutine object task_corotine at 0x000001918E9EB530>
# Wed Jul 12 14:39:11 2023 > Task-14, <coroutine object task_corotine at 0x000001918E9EB5A0>
# Wed Jul 12 14:39:11 2023 > Task-6, <coroutine object task_corotine at 0x000001918E9EAF80>
# Wed Jul 12 14:39:11 2023 > Task-15, <coroutine object task_corotine at 0x000001918E9EB610>
# Wed Jul 12 14:39:11 2023 > Task-2, <coroutine object task_corotine at 0x000001918E9615B0>
# Wed Jul 12 14:39:11 2023 > Task-5, <coroutine object task_corotine at 0x000001918E9E8970>
# Wed Jul 12 14:39:11 2023 > Task-16, <coroutine object task_corotine at 0x000001918E9EB680>
# Wed Jul 12 14:39:11 2023 > Task-7, <coroutine object task_corotine at 0x000001918E9EAFF0>
# Wed Jul 12 14:39:11 2023 > Task-17, <coroutine object task_corotine at 0x000001918E9EB6F0>
# Wed Jul 12 14:39:11 2023 > Task-8, <coroutine object task_corotine at 0x000001918E9EB220>
# Wed Jul 12 14:39:11 2023 > Task-18, <coroutine object task_corotine at 0x000001918E9EB760>
# Wed Jul 12 14:39:11 2023 > Task-4, <coroutine object task_corotine at 0x000001918E9E87B0>
# Wed Jul 12 14:39:11 2023 > Task-9, <coroutine object task_corotine at 0x000001918E9EB370>
# Wed Jul 12 14:39:11 2023 > Task-19, <coroutine object task_corotine at 0x000001918E9EB7D0>
# Wed Jul 12 14:39:11 2023 > Task-3, <coroutine object task_corotine at 0x000001918E9E85F0>
# Wed Jul 12 14:39:11 2023 > Task-10, <coroutine object task_corotine at 0x000001918E9EB3E0>
# Wed Jul 12 14:39:11 2023 > Task-20, <coroutine object task_corotine at 0x000001918E9EB840>
# Wed Jul 12 14:39:11 2023 > Task-11, <coroutine object task_corotine at 0x000001918E9EB450>
# Wed Jul 12 14:39:11 2023 > Task-21, <coroutine object task_corotine at 0x000001918E9EB8B0>
# Wed Jul 12 14:39:11 2023 > Task-12, <coroutine object task_corotine at 0x000001918E9EB4C0>