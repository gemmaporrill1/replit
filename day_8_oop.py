# Encapsulation


# class Bank2:
#     # Class variable | All your instances share the same value | class variable
#     interest_rate = 0.02

#     def __init__(self, acc_no, name, balance): # self points to the class name
#         # instance variables | different values in every instance
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

#     # instance method
#     def display_balance(self):
#         return f"Your balance is: R{self.balance:,}"

#     def withdraw(self, withdraw_amount):
#         if self.balance - withdraw_amount > 0:
#             self.balance -= withdraw_amount
#             return f"Success. {self.display_balance()}"
#         else:
#             return f"Insufficient funds"

#     def deposit(self, deposit_amount):
#         if deposit_amount > 0:
#             self.balance += deposit_amount
#             return f"Successfully deposited. {self.display_balance()}"
#         else:
#             return f"You cannot deposit negative amounts"

#     def apply_interest(self):
#         self.balance += Bank2.interest_rate * self.balance
#         return self.balance


# gemma = Bank2(123, "Gemma Porrill", 15_000)
# dhara = Bank2(124, "Dhara Kara", 50_001)
# caleb = Bank2(125, "Caleb Potts", 100_000)

# gemma.apply_interest()
# caleb.apply_interest()
# dhara.apply_interest()

# print(gemma.display_balance())
# print(dhara.display_balance())
# print(caleb.display_balance())

# Encapsulation extension | putting all methods and variables into one container | giving access to required variables


# class Bank3:
#     # Class variable | All your instances share the class variable
#     interest_rate = 0.02

#     def __init__(self, acc_no, name, balance):
#         # instance variables
#         self.acc_no = acc_no
#         self.name = name
#         self.__balance = balance  # self.__balance -> private variable

#     # instance method
#     def display_balance(self):
#         return f"Your balance is: R{self.__balance:,}"

#     # public methods
#     def withdraw(self, withdraw_amount):
#         if self.__balance - withdraw_amount > 0:
#             self.__balance -= withdraw_amount
#             return f"Success. {self.display_balance()}"
#         else:
#             return f"Insufficient funds"

#     def deposit(self, deposit_amount):
#         if deposit_amount > 0:
#             self.__balance += deposit_amount
#             return f"Successfully deposited. {self.display_balance()}"
#         else:
#             return f"You cannot deposit negative amounts"

#     def apply_interest(self):
#         self.__balance += Bank3.interest_rate * self.__balance
#         return self.__balance


# gemma = Bank3(123, "Gemma Porrill", 15_000)
# dhara = Bank3(124, "Dhara Kara", 50_001)
# caleb = Bank3(125, "Caleb Potts", 100_000)

# print(gemma.display_balance())


# # class methods | able to access across all classes
# class Bank4:
#     # Class variable | All your instances share the class variable
#     interest_rate = 0.02
#     accounts = 0

#     def __init__(self, acc_no, name, balance):
#         # instance variables
#         self.acc_no = acc_no
#         self.name = name
#         self.__balance = balance  # self.__balance -> private variable
#         Bank4.accounts += 1

#     # common methods across instances
#     # class method | cls -> Class
#     @classmethod
#     def update_interest_rate(cls, rate):
#         cls.interest_rate = rate


#     # static methods -> no cls or self | normal function
#     @staticmethod
#     def get_total_no_accounts():
#         return f"In total, we have {count} accounts"

#     # instance method| self will point to instance
#     def display_balance(self):
#         return f"Your balance is: R{self.__balance:,}"

#     # public methods
#     def withdraw(self, withdraw_amount):
#         if self.__balance - withdraw_amount > 0:
#             self.__balance -= withdraw_amount
#             return f"Success. {self.display_balance()}"
#         else:
#             return f"Insufficient funds"

#     def deposit(self, deposit_amount):
#         if deposit_amount > 0:
#             self.__balance += deposit_amount
#             return f"Successfully deposited. {self.display_balance()}"
#         else:
#             return f"You cannot deposit negative amounts"

#     def apply_interest(self):
#         self.__balance += Bank4.interest_rate * self.__balance
#         return self.__balance


# gemma = Bank4(123, "Gemma Porrill", 15_000)
# dhara = Bank4(124, "Dhara Kara", 50_001)
# caleb = Bank4(125, "Caleb Potts", 100_000)


# print(gemma.display_balance())

# Bank4.update_interest_rate(0.1)  # updating class variables using class methods

# # apply interest
# caleb.apply_interest()

# print(caleb.display_balance())

# # task
# # Bank4.get_total_account()

# print(Bank4.get_total_no_accounts(Bank4.accounts))


# exercise
class Circle:
    pi = 3.14159  # class variable

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = Circle.pi * self.radius**2
        return area

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def perimeter(radius):
        perimeter = 2 * Circle.pi * radius
        return perimeter


# task 1:
# static methods
print(Circle.perimeter(10))

# task 2:
circle1 = Circle(2)
print(circle1.calculate_area())

circle_from_dia = Circle.from_diameter(10)
print(circle_from_dia)


# Inheritance: Animal (Base) (name, speak) -> Dog (Child) (name, speak, run)
class Animal:
    def __init__(self, name):
        self.name = name

    # methods / attributes
    def speak(self):
        return " Some sound"


class Dog(Animal):

    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def run(self):
        return "wags tail"

    # Polymorphism | overriding method -> redefining in child class
    def speak(self):
        return " Woof woof"

    def speed_bonus(self):
        return f"Running at {self.speed * 2}km/h"


toby = Animal("Toby")

maxy = Dog("maxy", 20)

print(toby.speak())
print(maxy.speak())
print(maxy.run())
# print(toby.run()) error | only in child class
print(maxy.speed_bonus())


class Bank:
    # Class variable | All your instances share the class variable
    interest_rate = 0.02
    accounts = 0

    def __init__(self, acc_no, name, balance):
        # instance variables
        self.acc_no = acc_no
        self.name = name
        self.balance = balance  # self.__balance -> private variable
        Bank.accounts += 1

    # common methods across instances
    # class method | cls -> Class
    @classmethod
    def update_interest_rate(cls, rate):
        Bank.interest_rate = rate

    # static methods -> no cls or self | normal function
    @staticmethod
    def get_total_no_accounts(cls, count):
        Bank.accounts = count
        return f"In total, we have {count} accounts"

    # instance method| self will point to instance
    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"

    # public methods
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

    def apply_interest(self):
        self.balance += self.interest_rate * self.balance
        return self.balance


# savings account - interest_rate = 0.05
class SavingsAccount(Bank):

    interest_rate = 0.05

    def __init__(self, acc_no, name, balance):
        super().__init__(acc_no, name, balance)

    # def apply_interest(self):
    #     self.balance += SavingsAccount.interest_rate * self.balance
    #     return self.balance

    # def apply_interest(self):
    #     SavingsAccount.interest_rate = 0.05
    #     return self.balance


# Task 1
gemma = SavingsAccount(123, "Gemma Porrill", 1_000)
print(gemma.apply_interest())
# gemma.apply_interest()

gemma.display_balance()  # 1_050

# # checking account - withdraw R1
# class CheckingAccount(Bank):

#     withdraw_fee = 1

#     def withdraw(self, withdraw_amount):
#         return super().withdraw(withdraw_amount + CheckingAccount.withdraw_fee)


# # SavingsAccount -  interest_rate = 0.05


# # Task 2
# # CheckingAccount - withdraw  R1
# alex = CheckingAccount(126, "Alex Lazarus", 100)
# print(alex.withdraw(50))
# #  49


# magic methods __repr__, __str__, __add__


# checking account - withdraw R1
class CheckingAccount(Bank):

    withdraw_fee = 1

    def withdraw(self, withdraw_amount):
        return super().withdraw(withdraw_amount + CheckingAccount.withdraw_fee)

    def __str__(self):  # overriding object def with a string that imporves readability
        """Human readable output | Most important one"""
        return f"This account belongs to Account: {self.name}"

    def __repr__(self):
        """DX: String -> Class"""
        return f"CheckingAccount({self.acc_no}, '{self.name}', {self.balance})"

    def __add__(self, other):
        """Override when + is called"""
        return self.balance + other.balance


# SavingsAccount -  interest_rate = 0.05


# Task 2
# CheckingAccount - withdraw  R1
alex = CheckingAccount(126, "Alex Lazarus", 100)
caleb = CheckingAccount(126, "Caleb Potts", 100)

print(alex.withdraw(50))
#  49

print(alex)  # alex.__str__()

# protected variable = _name | one underscore
# private variable = __name | two underscore

print(alex.__repr__())

# shouldn't use dunder methods ^^

print(repr(alex))

print(alex + caleb)
