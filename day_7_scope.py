price = 100

def get_price():
    print("The price is: ", price)

get_price()

# scope - lifetime of variable

# lexical scope

# closure = own scope + lexical scope

code_word = "Hulk"

def space_ship():
    question = "Provide the code word"

    def code_word_check():
        password = "Hulk"
        print(question)

        if(password == code_word):
            print(f"Welcome, {password} is the")
        else:
            print(f"access denied")
    code_word_check()
space_ship() # always start at the function call

# closure has to happen for currying
# currying
def add(x):
    def add1(y):
        return x + y
    return add1

# print(add(10)) # returns a function
print(add(10)(5))

# using lambda with currying
# closure

add = lambda x: (lambda y: x + y)

# Default value copy by reference

def fun(nums=[]):
    nums.append(10)
    print(nums)

fun() # [10]
fun() # [10, 10]
fun() # [10, 10, 10]
fun() # [10, 10, 10, 10]


#exercise
def fun(nums=None): 
    if nums is None: 
        nums = [] 
    nums.append(10) 
    print(nums)

fun()
fun()
fun()
fun()


