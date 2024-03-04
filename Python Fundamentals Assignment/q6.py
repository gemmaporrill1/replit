# Setup Code
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100},
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.

sales_grouped = {}

for sale in sales:
    name = sale["salesperson"]
    amount_total = sale["amount"]
    if name in sales_grouped:
        sales_grouped[name] += amount_total
    else:
        sales_grouped[name] = amount_total

print(sales_grouped)
