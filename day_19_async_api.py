import asyncio
import requests
import aiohttp
from pprint import pprint
from time import time

TOKEN = "604b93c64af04795b6993000241503"


# Sync
# def get_city_temp(city_name):
#     response = requests.get(
#         f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
#     )
#     weather_response = response.json()

#     return weather_response["location"]["name"], weather_response["current"]["temp_c"]


# print(get_city_temp("Cape Town"))
# print(get_city_temp("Johannesburg"))
# print(get_city_temp("Durban"))
# print(get_city_temp("Chennai"))


# async def get_city_temp(city_name):


# async - aiohttp | much faster ->pushed into a event loop
# async def get_city_temp(city_name):
#     # print(f"Getting temp of {city_name}")
#     # await asyncio.sleep(2)
#     url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
#     # memory management - error
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             weather = await response.json()
#             print(
#                 f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']} Celsius"
#             )


# async def main():
# await get_city_temp("Cape Town")
# await get_city_temp("Johannesburg")
# await get_city_temp("Dublin")

#     # task 1
#     task1 = asyncio.create_task(get_city_temp("Johannesburg"))  # co-currently
#     task2 = asyncio.create_task(get_city_temp("Cape Town"))  # co-currently
#     task3 = asyncio.create_task(get_city_temp("Durban"))

#     # task 2
#     all_tasks = [
#         asyncio.create_task(get_city_temp("Johannesburg")),
#         asyncio.create_task(get_city_temp("Cape Town")),
#         asyncio.create_task(get_city_temp("Durban")),
#     ]

#     # asyncio.run(main())

#     # asyncio.run(get_city_temp("Cape Town"))
#     # asyncio.run(get_city_temp("Chennai"))
#     # asyncio.run(get_city_temp("Johannesburg"))
#     # asyncio.run(get_city_temp("Durban"))
#     # asyncio.run(get_city_temp("Dublin"))
#     # task 1
#     await asyncio.gather(task1, task2, task3)
#     # task 2
#     await asyncio.gather(*all_tasks)


# asyncio.run(main())


# task 3

# async def main():
#     cities = [
#         "New York",
#         "Tokyo",
#         "London",
#         "Paris",
#         "Dubai",
#         "Singapore",
#         "Sydney",
#         "Istanbul",
#         "Hong Kong",
#         "Cape Town",
#     ]
#     await asyncio.gather(*[get_city_temp(city) for city in cities])


# start_time = time()
# asyncio.run(main())
# end_time = time()

# print(f"Time take: {end_time - start_time}")


# task 4


# async def main():
#     cities = [
#         "New York",
#         "Tokyo",
#         "London",
#         "Paris",
#         "Dubai",
#         "Singapore",
#         "Sydney",
#         "Istanbul",
#         "Hong Kong",
#         "Cape Town",
#     ]

#     all_cities_task = {city: await get_city_temp(city) for city in cities}
#     return all_cities_task


# start_time = time()
# result = asyncio.run(main())
# end_time = time()

# pprint(dict(result))


# print(f"Time taken: {end_time - start_time} seconds")


# async def main(cities):
#     temperatures = await asyncio.gather(*[get_city_temp(city) for city in cities])
#     return dict(temperatures)


cities = [
    "New York",
    "Tokyo",
    "London",
    "Paris",
    "Dubai",
    "Singapore",
    "Sydney",
    "Istanbul",
    "Hong Kong",
    "Cape Town",
]

# temperatures = asyncio.run(main(cities))
# pprint(temperatures)


# ANSWER
async def get_city_name_temp(city_name):
    print(f"Getting temp of {city_name}")
    url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            return weather["location"]["name"], weather["current"]["temp_c"]


# Performance
async def main(cities):
    cities_data_co_current = [get_city_name_temp(city) for city in cities]
    cities_data = await asyncio.gather(*cities_data_co_current)
    pprint(dict(cities_data))

    cities = [
        "New York",
        "Tokyo",
        "London",
        "Paris",
        "Dubai",
        "Singapore",
        "Sydney",
        "Istanbul",
        "Hong Kong",
        "Cape Town",
    ]


asyncio.run(main(cities))
