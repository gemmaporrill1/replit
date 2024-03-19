import asyncio
import aiohttp
from pprint import pprint
from time import time


# async def get_user():
#     url = "https://65f8283cb4f842e8088712ef.mockapi.io/users"

#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             return users


# async def main():
#     users_data = await get_user()
#     user_names = [user["name"] for user in users_data]
#     print("\n".join(user_names))


# start_time = time()
# asyncio.run(main())
# end_time = time()

# print(f"Time take: {end_time - start_time}")


# delete first 5 users with async


# async def get_user():
#     url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users"

#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             user_ids = [user["id"] for user in users]
#             return user_ids


# async def delete_user_by_id(id):
#     url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users/{id}"

#     async with aiohttp.ClientSession() as session:
#         async with session.delete(url) as response:
#             deleted_users = await response.json()
#             return deleted_users


# async def main():
#     user_ids = await get_user()
#     delete_user_tasks = [delete_user_by_id(id) for id in user_ids[:5]]
#     deleted_users = await asyncio.gather(*delete_user_tasks)

#     pprint(deleted_users)


# asyncio.run(main())


# async returns -> co-routine
# async def create_user(new_user):
#     print(new_user)
#     url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users/{id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=new_user) as response:
#             user = await response.json()
#             return user


# async def main():
#     new_user = {"name": "Gemma Porrill", "avatar": "string"}
#     await create_user(new_user)


# asyncio.run(main())


# # task 2
# # change user's avatar to flag


async def get_users():
    url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            users = await response.json()
            return users


# async def update_user(update_user):
#     url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users/{id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.put(url, json=update_user) as response:
#             user = await response.json()
#             return user


# async def main():
#     user_ids = await get_user()
#     update_user = {
#         "avatar": "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
#     }
#     update_tasks = [update_user(id) for id in user_ids]
#     updated_users = await asyncio.gather(*update_tasks)
#     print("Users updated successfully:", updated_users)


# asyncio.run(main())

# task 3 - create 5 users


# async def get_user():
#     url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             return users


# async def create_users(new_users):
#     url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=new_users) as response:
#             return await response.json()


# async def main():
#     new_users = [
#         {"name": "Alex"},
#         {"name": "Gemma"},
#         {"name": "Thato"},
#         {"name": "Lilitha"},
#         {"name": "Dhara"}
#     ]

#     users_data = await create_users(new_users)
#     print(users_data)


# asyncio.run(main())


# async def main():
#     user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
#     flag = (
#         "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
#     )

#     user_co_routines = []

#     for user_name in user_list:
#         new_user = {
#             "name": user_name,
#             "avatar": "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain",
#         }
#         user_co_routines.append(create_users(new_user))
#     users_data = await asyncio.gather(*user_co_routines)
#     print(users_data)


# asyncio.run(main())


# async def main():
#     user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
#     flag = (
#         "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
#     )
#     #Concurrent with coroutines
#     user_co_routines = []

#     for user_name in user_list:
#         new_user = {
#             "name": user_name,
#             "avatar": "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain",
#         }
#         user_co_routines.append(create_users(new_user))
#     users_data = await asyncio.gather(*user_co_routines)
#     print(users_data)


# asyncio.run(main())

# # list comprehension
# async def main():
#     user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
#     flag = (
#         "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
#     )

#     user_co_routines = [
#         create_users({"name": user_name, "avatar": flag}) for user_name in user_list
#     ]
#     users_data = await asyncio.gather(*user_co_routines)
#     print(users_data)


# asyncio.run(main())


# async def get_user():
#     url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             return users


async def update_users(users):
    url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users"
    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=users) as response:
            return await response.json()


async def main():
    users = await get_users()
    user_ids = [user["id"] for user in users]
    flag = (
        "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
    )
    update_user = {"avatar": flag}
    updated_users = await asyncio.gather(*update_user)
    print(updated_users)


asyncio.run(main())


# updating one user
async def update_user(updated_data, id):
    print(updated_data)
    url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=updated_data) as response:
            return await response.json()


async def main():
    flag = (
        "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
    )
    updated_data = {"name": "Gemma Porrill", "avatar": flag}
    user_id = 17
    result = await update_user(updated_data, user_id)
    print(result)


asyncio.run(main())


# updating multiple users
# updating one user
async def update_user(updated_data, id):
    print(updated_data)
    url = f"https://65f8283cb4f842e8088712ef.mockapi.io/users/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=updated_data) as response:
            return await response.json()


async def main():
    flag = (
        "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
    )
    updated_data = {"avatar": flag}
    users = await get_users()
    update_user_co_current = [update_user(updated_data, user["id"]) for user in users]
    result = await asyncio.gather(update_user_co_current)
    print(result)


asyncio.run(main())
