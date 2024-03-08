import json

data = {
    "employees": [
        {"name": "Alice", "age": 30, "department": "Sales"},
        {"name": "Bob", "age": 25, "department": "Marketing"},
    ]
}

print(data)

data_json = json.dumps(data)  # dumps = covert dict to json

print(data_json, type(data_json))


# multi line string not a dictionary/list
# JSON - JavaScript Object Notation - string
# serializable (converting) | cannot covert dict if it contains a function -> Invalid JSON

student_json = """
        {
            "name": "Gemma",
            "gender": "Female"
        }
"""

student = json.loads(student_json)  # loads = covert json to dict

print(type(student))


# task 1

bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""

bank_dict = json.loads(bank_data)


# def activity():
#     for user in bank_dict:
#         if user["isActive"] == True:
#             user["balance"] += 0.1 * user["balance"]
#     return bank_dict


# bank_json = json.dumps(activity())
# print(bank_json)


# task 2 list comprehension

interest = 1.1

accounts = [
    (
        {**account, "balance": account["balance"] * interest}
        if account["isActive"]
        else account
    )
    for account in bank_dict
]

bank_json = json.dumps(accounts, indent=4)
print(bank_json)

# writing a json file
with open("bank_dict.json", "w") as file:
    json.dump(accounts, file, indent=4)

# reading a json file
with open("bank_dict.json", "r") as file:
    data = json.load(file)
    print(data, type(data))  # prints a list


