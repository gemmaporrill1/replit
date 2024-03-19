import asyncio


# mark as async -> it forces execution
# async def hello_world():
#     print("started")
#     await asyncio.sleep(3)  # waits for three sec | sleep -> inbuilt async function
#     print("Hello world")


# asyncio.run(hello_world())

# task 1 -  count down
# 3, 2, 1, Happy new year


# async def countdown():
#     print("3")
#     await asyncio.sleep(1)
#     print("2")
#     await asyncio.sleep(1)
#     print("1")
#     await asyncio.sleep(1)
#     print("Happy New Year")


# asyncio.run(countdown())

# task 2 - improving solution
# create a reuseable async function, DRY


# async def countdown_async(count):
#     for sec in range(count, 0, -1):
#         print(sec)
#         await asyncio.sleep(1)
#     print("Happy New Year")


# asyncio.run(countdown_async(3))


# task 3 - without any loop or recursion

# async def countdown_async(count):
#     if count > 0:
#         print(count)
#         await asyncio.sleep(1)
#         await countdown_async(count - 1)
#     else:
#         print("Happy New Year!")


# asyncio.run(countdown_async(3))

# asyncio.run(countdown_async(5))

# every async function returns a coroutine

# Event Loop: behind the async function


# def add(x):
#     return x + 1


# def sum(a, b):
#     c = add(a) + add(b)
#     return c


# print(sum(3, 5))

# returns or function finishes -> will be popped off the stack

# event loop will only be pushed to the stack when it becomes empty | push condition


async def cooking_eggs():
    print("crack eggs into pan")
    await asyncio.sleep(3)
    print("eggs cooked")
    return f"Data - Eggs"


async def make_coffee():
    print("Coffee brewing")
    await asyncio.sleep(2)
    print("coffee done")
    return f"Data - Coffee"


async def make_cereal():
    print("cereal pouring")
    await asyncio.sleep(2)
    print("cereal done")
    return f"Data - Cereal"  # collecting data


# async function with event loop
async def main():
    # request to event loop to schedule the task
    # task1 = asyncio.create_task(cooking_eggs())  # co-currently
    # task2 = asyncio.create_task(make_coffee())  # co-currently
    # task3 = asyncio.create_task(make_cereal())

    # all_tasks = [task1, task2, task3]

    # into a list | returns coroutines
    # already scheduled
    all_tasks = [
        asyncio.create_task(cooking_eggs()),
        asyncio.create_task(make_coffee()),
        asyncio.create_task(make_cereal()),
    ]

    # request to event loop to schedule
    all_co_routines = [
        cooking_eggs(),
        make_coffee(),
        make_cereal(),
    ]

    # waiting for the background_task
    print("Toast 1")
    print("Toast 2")
    print("Toast 3")
    print("Toast 4")
    # this allows for eggs cooked to be printed first and relating to the longest task
    # await - when you use another async function in a async function
    # await task1

    # when you don't know which one is longer | waits until the longest one completes
    # await asyncio.wait({task1, task2}) # takes in a set of tasks

    # await asyncio.gather(task1, task2)

    # await asyncio.gather(*all_tasks)

    # collecting data together
    # order of data = order given in
    data = await asyncio.gather(*all_tasks)
    print(data)  # prints a list of all the data


asyncio.run(main())
