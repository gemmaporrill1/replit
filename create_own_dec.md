# Create own decorator
## Decorator explaination
- Python decorators allow to change the behavior of a function without modifying the function itself
- Functions are taken as the argument into another function and then called inside the wrapper function
- applied using the `@decorator` syntax

## Creation
    def my_decorator(func):
    def wrapper(number):
        print("Something is happening before the function is called.")
        result = func(number)
        print("Something is happening after the function is called.")
        return result
    return wrapper
    @my_decorator
    def calculate_square(number):
        result = number ** 2
        print(f"The square of {number} is {result}")
        return result
- Output: 
```
Something is happening before the function is called.
The square of 5 is 25
Something is happening after the function is called.
```

## Explaination

1. The @my_decorator syntax applies the my_decorator to the calculate_square function.
2. When you call calculate_square(5), it is equivalent to calling the wrapper function created by the decorator
3. The wrapper function first prints the message before the original function is called.
4. It then calls the original calculate_square function, which prints the square calculation message.
5. Finally, the wrapper function prints the message after the original function is called.

