# Gemma Porrill Currying and Partials assignment 
## Currying
- term “Curry” comes from the name of the mathematician Haskell Curry
- Currying is used to transform multiple-argument function into single argument function by evaluating incremental nesting of function arguments
- enhances modularity -> breaking down the code into smaller, independent, and interchangeable parts or modules
- example
- ` def curry_multiply(a):
    def next(b):
        def final(c):
            return a * b * c
        return final
    return next
  curry_multiply(2)(3)(4)`
- takes one argument at a time but gives the correct output by multiplying the three numbers together
- important role in building data pipelines
  - in machine learning projects
- useful when working with higher order functions

## Partials
- from functools import partial
- Partial function application is another way to perform a form of currying
- example
- `import functools
    def multiply(a, b, c):
        return a * b * c
    multiply_by_two = functools.partial(multiply, 2)
    multiply_by_two_and_three = functools.partial(multiply_by_two, 3)
    result = multiply_by_two_and_three(4)  
    result`
- It fixes a number of arguments to a function, producing a new function with fewer arguments
- Useful when you need to repeatedly call a function with certain arguments fixed or when you want to adapt a function to fit into a context that expects a different number of arguments
- Used for simpler use cases to make the code more readbale 