# Setup Code
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.

merged_list = [
    {**employee, **salary}
    for employee in employees
    for salary in salaries
    if employee["id"] == salary["id"]
]

print(merged_list)
