#scenario | this is repetition of logic

# a = 8
# b = 10

# print("The sum is:", a + b)

# a1 = 7
# b1 = 16

# print("The sum is:", a1 + b1)

# a2 = 10
# b2 = 3

# print("The sum is:", a2 + b2)

#solve this problem by using functions

#functions pack your logic together

# full thing -> declaration / definition 
# def sum(a, b): # sum -> function name | (a, b) -> parameters/arguments
#   return a + b # function body

# abstracted the logic | hiding implemetation

# use | abstraction (hiding)
# call the logic multiple times
# print("The sum is:", sum(30, 50))

# default values (argument) should come at the last, 
# can't have it in the front and not in the middle
def driving_test(name, age, car="Toyota tazz"): 
  if age >= 18:
    return f"{name} You are eligible for driving. You will be tested with {car}"
  else:
    return "Try again in a few years"

# print(driving_test("Caleb", 20, "GR Corolla")) | function call
# print(driving_test(10))
# print(driving_test("Gemma", 20))
#other ways to define a functions

#types of argument
# position argument | order matters
print(driving_test("Gemma", 20))
# keyword argument 
print(driving_test(age = 21, name = "Dhara"))
