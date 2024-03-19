# Iterables -> __iter__ | which can be looped many times | list | Doesn't know where I am in loop
# Iterator => __next__ & __iter__ | can only loop once | saves alot of memory | Doesn't know where I am in loop

# Why?

# nums = [5, 10, 20]
# print(dir(nums))  # dir gives all methods/dunder methods possible in your list


# how to get a iterator

# nums_iter = nums.__iter__()  # converts to iterator from iterable

# number_iter = iter(nums)  # preferred way

# print(dir(number_iter))  # Iterator ->  __next__ & __iter__

# # Conclusion: All iterators are Iterables | But not the other way around

# print(next(number_iter))  # 5
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))

# create an Iterator and loop with while loop

# num = [2, 3, 4]

# num_iter = iter(num)

# while True:
#     try:
#         print(next(num_iter))
#     except StopIteration:
#         break


# num_iter1 = iter([2, 3, 4])
# for num in num_iter1:
#     print(num)


# range(0, 100000, 1) # holds only the three values | a list will occupy alot of space if there are 10000 values
# iterator only remembers one thing at a time | save memory | infinite lists

# iterator from scratch:


# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     # return same value | only this | range already an iter
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.start > self.end:
#             raise StopIteration
#         self.start += 1
#         return self.start - 1


# for n in MyRange(1, 5):
#     print(n)


# Generator - clean | infinite_ingeters() -> return iterator with yield | Lazy until you call the next it doesn't get invoked
# more concise and cleaner than manually creating
# Generator syntax - yield

# def infinite_integers():
#     n = 0
#     while True: # loop never ending due to true
#         yield n # return value n then pause until yield is called again
#         n += 1


# infinite = infinite_integers() # infinite is an iterator here
# print(next(infinite)) # 0
# print(next(infinite)) # 1
# print(next(infinite)) # 2


# Task - fibonacci generator function


def fibonacci(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        sum = a + b
        a = b
        b = sum


for num in fibonacci(10):
    print(num)

# print(next(fibonacci(10)))
