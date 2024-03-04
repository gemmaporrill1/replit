from pprint import pprint

# Setup Code
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400},
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.

product_list = list(
    filter(
        lambda product: product["price"] <= 500
        and product["category"] == "Electronics",
        products,
    )
)

pprint(product_list)
