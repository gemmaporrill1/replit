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

# def sayHello():
#   def msg():
#     return 'Hello, Gemma'
#   return msg

# # task 1

# msg_fun = sayHello()
# print(msg_fun())

# #task 2

# print(sayHello()()) # prints "Hello, Gemma"

#task 3
# 3 6 -> 18
# implicit return | factory function
# paradigm (styles)
# functional programming - F#, Haskel (no loops, instead recursion) | currying, partials = ASSIGNMENT
# OOP - inheritence
# procedural programming
# mathematical programming 

#functional 
mul = lambda x: lambda y: x * y # right hand side of : is what is returned
# lambda x: (lanmbda y: (x * y)) | reads like this left to right
print(mul(3)(6))

#reusability 
mul_5 = mul(5)
print(mul_5, type(mul_5)) # -> type is function 
print(mul_5(10)) # prints final value

#HOF - argument function
result1 = map(lambda x: x * 2, [10, 20, 30])
result2 = filter(lambda x: x > 10, [10, 50, 60, 100, 6, 8, 30])

print(list(result1))
print(list(result2))

#pythonic way - list comprehension but complex lambda

# sequence - list
# 1. len
# 2. sum
# 3. sorted
# 4. max
# 5. min

print(sum([10, 30, 60]))
print(max([10, 100, 30, 60]))
print(min([10, -1, 30, 60]))

print(all([True, False, True])) # and
print(any([True, False, True])) # or


print(any([10, 0, 30, -1]))

# falsy values: | when converted to boolean they will be False | others are truthy
# 1. 0
# 2. []
# 3. None
# 4. {}
# 5. ""
# 6. set()
# 7. ()
# 8. False

x = []

if(x):
  print('cool')
else:
  print('super')