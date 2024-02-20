# #task 1
# stock1 = "vanilla"
# stock2 = "lime"
# stock3 = "chocolate"

# choice = input("Please choose your flavour: ")

# #DRY - don't repeat yourself

# # lime
# # yes it is available

# #strawberry
# # no we don't have in stock

# #try 1

# if (choice == stock1 or choice == stock2 or choice == stock3):
#   print("It is available")
# else:
#   print("It is unavailable")

#task 2 - in operator | membership operator | boolean

shop_stock = "vanilla, lime, chocolate"

choice = input("Please choose your flavour: ")

# if (choice in shop_stock):
#   print("It is available")
# else:
#   print("It is unavailable")

# refactor -> code quality

# ternary operator ( 3 operands )
# condition if ___ else ___

# binary operators ( 2 operands )
# Comparison >, <, ==, >=, <=, !=
# and, or
# Arithmetic +, -, *, /

# = assignment operator

# unary operators ( 1 operand )
# not

#task 3 

#change to ternary

print('it is available' if choice in shop_stock else 'it is unavailable')
