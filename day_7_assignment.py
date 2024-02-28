# transaction assignment

# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000


class Transactions:
    def __init__(self):
        self.transactions = []

    def withdraw(self, id, date, withdraw_amount):
        transaction = {
            "id": id,
            "date": date,
            "type": "withdraw",
            "amount": withdraw_amount,
        }
        self.transactions.append(transaction)
        return f"Success. Your balance is: R{withdraw_amount:,}"

    def deposit(self, id, date, deposit_amount):
        transaction = {
            "id": id,
            "date": date,
            "type": "deposit",
            "amount": deposit_amount,
        }
        self.transactions.append(transaction)
        return f"Success. Your balance is R:{deposit_amount:,}"

    def display_transactions(self):
        print("{:<5} {:<10} {:<10} {:<10}".format("ID", "Date", "Type", "Amount"))
        for transaction in self.transactions:
            print(
                "{:<5} {:<10} {:<10} R{:<10,}".format(
                    transaction["id"],
                    transaction["date"],
                    transaction["type"],
                    transaction["amount"],
                )
            )


gemma = Transactions()
gemma.withdraw(1, "29 Feb", 2000)
gemma.deposit(2, "1 Mar", 6000)
gemma.deposit(3, "3 Mar", 7000)

gemma.display_transactions()
