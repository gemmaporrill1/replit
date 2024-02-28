# Object Oriented Programming

# Car
# 1. engine
# 2. wheels
# 3. doors
# 4. name


# car

# 1. engine - v8
# 2. wheels - 4
# 3. doors - 2
# 4. name - ferrari

# Toyota tazz
# 1. engine - v4
# 2. wheels - 4
# 3. doors - 4
# 4. name - toyota tazz

# class Car:
#     pass

# ferrari = Car()
# ferrari.name = "Ferrari"
# ferrari.engine = "v8"
# ferrari.wheels = 4
# ferrari.doors = 2

# toyota = Car()
# toyota.name = "Toyota"
# toyota.engine = "v8"
# toyota.wheels = 4
# toyota.doors = 2

# print(ferrari.name, ferrari.doors)
# print(toyota.name, toyota.doors)


# Car -> blueprint | class blueprint object
# class Car:
#     def __init__(self):
#         self.name = "Ferrari"
#         self.engine = "v8"
#         self.wheels = 4
#         self.doors = 2


# # self -> to the object created | hard coding
# # ferrari -> object
# # dry
# # __init__ -> first methods create an object
# class Car:
#     def __init__(self, name, engine, wheels, doors):
#         self.name = name
#         self.engine = engine
#         self.wheels = wheels
#         self.doors = doors

#     def horn(self):
#         return "Vroom vroom"


# ferrari = Car("Ferrari", "v8", 4, 2)
# toyota = Car("Toyota", "v4", 4, 4)
# bmw = Car("BMW", "v6", 4, 4)
# ford = Car("Ford", "v6", 4, 2)


# print(ferrari.name, ferrari.wheels)
# print(toyota.name, toyota.wheels)
# print(ferrari.horn())
# print(toyota.horn())

# Bank account
# 1. acc_no
# 2. name
# 3. balance


# task 1 - create a class and have methods
class Bank1:
    def __init__(self, acc_no, name, balance):
        # instance variables
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"

    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount > 0:
            self.balance -= withdraw_amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds"

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
            return f"Successfully deposited. {self.display_balance()}"
        else:
            return f"You cannot deposit negative amounts"


gemma = Bank1(123, "Gemma Porrill", 15_000)
dhara = Bank1(124, "Dhara Kara", 50_001)
caleb = Bank1(125, "Caleb Potts", 100_000)

# task 2
print(gemma.display_balance())

# task 3
print(caleb.withdraw(2000))
print(caleb.display_balance())

# task 4
print(dhara.deposit(10_000))
print(dhara.display_balance())


# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000
