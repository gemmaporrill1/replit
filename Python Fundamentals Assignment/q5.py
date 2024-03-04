# Setup Code
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"},
]
# Expected Task: Summarize the total amount spent per category.

total_amount_dict = {}

for transaction in transactions:
    category_name = transaction["category"]
    amount_spent = transaction["amount"]
    if category_name in total_amount_dict:
        total_amount_dict[category_name] += amount_spent
    else:
        total_amount_dict[category_name] = amount_spent

# Optionally, if you want to print the final dictionary after processing all transactions:
print("Final total amounts per category:", total_amount_dict)
