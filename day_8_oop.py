# Encapsulation


class Bank2:
    # Class variable | All your instances share the class variable
    interest_rate = 0.02

    def __init__(self, acc_no, name, balance):
        # instance variables
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    # instance method
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

    def apply_interest(self):
        self.balance += Bank2.interest_rate * self.balance
        return self.balance


gemma = Bank2(123, "Gemma Porrill", 15_000)
dhara = Bank2(124, "Dhara Kara", 50_001)
caleb = Bank2(125, "Caleb Potts", 100_000)

gemma.apply_interest()
caleb.apply_interest()
dhara.apply_interest()

print(gemma.display_balance())
print(dhara.display_balance())
print(caleb.display_balance())

# Encapsulation extension | putting all methods and vairables into one container | giving access to required variables


class Bank3:
    # Class variable | All your instances share the class variable
    interest_rate = 0.02

    def __init__(self, acc_no, name, balance):
        # instance variables
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance  # self.__balance -> private variable

    # instance method
    def display_balance(self):
        return f"Your balance is: R{self.__balance:,}"

    # public methods
    def withdraw(self, withdraw_amount):
        if self.__balance - withdraw_amount > 0:
            self.__balance -= withdraw_amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds"

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance += deposit_amount
            return f"Successfully deposited. {self.display_balance()}"
        else:
            return f"You cannot deposit negative amounts"

    def apply_interest(self):
        self.__balance += Bank3.interest_rate * self.__balance
        return self.__balance


gemma = Bank3(123, "Gemma Porrill", 15_000)
dhara = Bank3(124, "Dhara Kara", 50_001)
caleb = Bank3(125, "Caleb Potts", 100_000)

print(gemma.display_balance())
