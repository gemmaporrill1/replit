# Iterables -> __iter__ | which can be looped many times | list
# Iterator => __next__ & __iter__ | can only loop once | save memory


# Why?

nums = [5, 10, 20]
print(dir(nums))  # dir gives all methods/dunder methods possible in your list


# how to get a iterator

nums_iter = nums.__iter__()  # converts to iterator fro  iterable

number_iter = iter(nums)  # preferred way

print(dir(number_iter))  # Iterator ->  __next__ & __iter__

# Conclusion: All iterators are Iterables | But not the other way around

print(next(number_iter))  # 5
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
