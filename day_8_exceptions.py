def math_divide(n1, n2):
    try:
        result = n1 / n2
        print("The answer is: ", result)

    except ZeroDivisionError:
        # when zerodivisionerror happens
        print("you cannot divide by zero")

    else:
        # when no errors happen
        print("Division was successful")

    finally:
        # no error or error - always runs | runs last
        print("Operation done")


# math_divide(10, 5)
# math_divide(20, 0)

# # Day 9

# math_divide("abc", 1)  # another error unsupported operator type

from datetime import datetime

# task 1
# 2000
# Your age is 24


def calculate_age():
    age = input("Please tell me your year of birth ")
    new_year = datetime.now().year
    calc_age = new_year - int(age)
    print("Your age is:", calc_age)


# task 2
# handle errors


# Runtime errors
def calc_age1():
    try:
        age = input("Please tell me your year of birth ")
        calc_age = datetime.now().year - int(age)
        print("your age is:", calc_age)

    except ValueError:
        print("Your input is in the incorrect format")

    else:
        print("Age calculated")

    finally:
        print("Calculation completed")


# Task 3 -ve values, future values | Logical error
def calc_age():
    try:
        age = int(input("Please tell me your year of birth "))
        birth_year = datetime.now().year

        # raise -> stops further execution
        # handling logical errors
        if age <= 0:
            raise ValueError("Cannot be negative")
        if age > birth_year:
            raise ValueError("cannot be from future")
        # code is shielded
        calc_age = birth_year - int(age)
        print("Your age is:", calc_age)

    except ValueError as err:
        print("Your input is in the incorrect format", err)

    # don't know what the error will be | catch all errors | don't use alot | try be more specific
    except Exception as err:
        print("This is my catch all", err)


# creating own error class
# inherit from exception
class NegativeNumbersError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "Negative numbers are not allowed"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.value} -> {self.message}"


def only_positive_numbers():
    try:
        x = -10
        if x < 0:
            raise NegativeNumbersError(x)
    except NegativeNumbersError as e:
        print(e)


if __name__ == "__main__":
    # calc_age()
    only_positive_numbers()
