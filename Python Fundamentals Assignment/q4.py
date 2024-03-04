# Setup Code
orders = [
    {
        "order_id": 1,
        "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
    },
    {
        "order_id": 2,
        "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
    },
]

# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.

product_dict = {}

for order in orders:
    products = order["items"]
    for product in products:
        name_key = product["product"]
        quantity_value = product["quantity"]
        if name_key in product_dict:
            product_dict[name_key] += quantity_value
        else:
            product_dict[name_key] = quantity_value

print(product_dict)
