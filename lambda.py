# one line function

# add = lambda a, b: a + b
# print(add(2,3))

#anonymous - nameless function
# one liner 
# implicitly return (automatically)

#function treated as first class citizen (value) | python

# 1. Assign a function to a variable
# 2. Pass a function as an argument
# 3. Return a function

# player_stats = [10, 20, 30]

# boosted_stats = map(lambda x: x * 2, player_stats)
# print(boosted_stats, list(boosted_stats))

#what does map do?
#applies a specified function into all items in the iterable


#higher order function | greeting() accepts an argument as a function
# def say_hello():
#   return "Hello, "

# def greeting(hello_message, name):
#   print(hello_message() + name)

# greeting(say_hello, "Gemma")

#how it will look in map

# def map_own(fn, arr):
#   result = []
#   for item in arr:
#     result.append(fn(item))
#   return result
  
# result = map_own(lambda x: x * 2, [10, 20, 30])
# print(result)


#list comprehension
# def map_own(fn, arr):
#   return [fn(val) for val in arr]

# print(map_own(lambda x: x * 2, [10, 20, 30]))
# print(map_own(lambda x: x * 2, [40, 50, 60]))

# map object -> lazy only when you need it does it apply the function
# more efficient 

# mul = lambda x: lambda y: x * y 

def sayHello():
  def msg():
    return 'Hello, Gemma'
  return msg

# task 1

msg_fun = sayHello()
print(msg_fun())

#task 2

print(sayHello()()) # prints "Hello, Gemma"

#task 3
# 3 6 -> 18
mul = lambda x: lambda y: x * y 
print(mul(3)(6))
