books = [
  {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
  {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
  {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
  {"title": "Sapiens", "rating": 4.9, "genre": "History"},
  {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]

#task 1
#all books that are highly rated 4.7 >=

# book_list = []

# for dictionary in books:
#   book_list.append(dictionary) #pass by reference
#   if dictionary["rating"] >= 4.7:
#     print(dictionary["title"])

#task 2 : list comprehension

# book_list = [dictionary["title"] for dictionary in books if dictionary["rating"] >= 4.7]
# print(book_list)

#task 3 
#A-Z order

# book_list = [dictionary["title"] for dictionary in books if dictionary["rating"] >= 4.7]
# # book_list.sort() #mutation happens
# print(sorted(book_list)) #sorts it and provides copy



#exercise 2
# task 1 - add to inventory

# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]

# name = input("What is the product name? " )
# quantity = input("What is the quantity? " )
# price = input("What is the price? " )

# new_product = {"name": name, "quantity": quantity, "price": price}

# inventory.append(new_product)

# print(inventory)

#task 2 - update inventory

# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]

# name = input("What is the product name? " )
# quantity = input("What is the quantity? " )
# price = input("What is the price? " )


# for product in inventory:
#   if product["name"] == name:
#     product["quantity"] += int(quantity)
#     product["price"] = float(price)

# print(inventory)

#answer for 2

# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]

# name = input("What is the product name? " )
# quantity = input("What is the quantity? " )
# price = input("What is the price? " )

# for item in inventory:
#   if(item['name'] == name):
#     item['quantity'] += quantity
#     item['price'] = price
#     break #stops the for loop

# print(inventory)

#task 3 not exist add to inventory

# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]

# name = input("What is the product name? " )
# quantity = input("What is the quantity? " )
# price = input("What is the price? " )


# for product in inventory:
#   if product["name"] == name:
#     product["quantity"] += int(quantity)
#     product["price"] = float(price)
#     break
# else:
#   new_product = {"name": name, "quantity": quantity, "price": price}
#   inventory.append(new_product)

# print(inventory)

#answer for 3

# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]

# name = input("What is the product name? " )
# quantity = input("What is the quantity? " )
# price = input("What is the price? " )

# new_product = {"name": name, "quantity": quantity, "price": price}

# item_found = False

# for item in inventory:
#   if(item['name'] == name):
#     item['quantity'] += quantity
#     item['price'] = price
#     item_found = True
#     break #stops the for loop

# if(item_found == False): #if(not item_found)
#   inventory.append(new_product)


# print(inventory)
  

# 5 pillars -> good quality
# 1: readability -> for loop to list comprehension makes it more readable
# 2: maintainability -> reuseable
# 3: extendability
# 4: testability
# 5: performance

# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]

# name = input("What is the product name? " )
# quantity = input("What is the quantity? " )
# price = input("What is the price? " )

# new_product = {"name": name, "quantity": quantity, "price": price}

# for item in inventory:
#   if(item['name'] == name):
#     item['quantity'] += quantity
#     item['price'] = price
#     break
#   #only when break does not happen then to else | for ... else 
# else:
#   inventory.append(new_product)

# print(inventory)

#exercise 3

#output
#people who are 21 or above and VIP123
#Blacklist people are not allow

#["Alice", "Charlie"]

guests = [
  {"name": "Alice", "age": 25, "code": "VIP123"},
  {"name": "Bob", "age": 17, "code": "VIP123"},
  {"name": "Charlie", "age": 30, "code": "VIP123"},
  {"name": "Dave", "age": 22, "code": "GUEST"},
  {"name": "Eve", "age": 29, "code": "VIP123"}
]

blacklist = ["Dave", "Eve"]

allowed_guests = []

# for guest in guests:
#   if guest["name"] in blacklist:
#     continue
#   if guest["age"] >= 21 and guest["code"] == "VIP123":
#     allowed_guests.append(guest)
#     print(guest["name"])
  
# print(allowed_guests)

#answer

#CONSTANT_CASE
PASS_CODE = "VIP123"

for guest in guests:
  if(guest["age"] >= 21 and guest["code"] == PASS_CODE 
     and guest["name"] not in blacklist):
    allowed_guests.append(guest["name"])
print(allowed_guests)

#PEP - Python Enhancement Proposal 8 | guidlines for writing python

#filters in the list comprehension come last (if statement)
#what you want to print comes first

guestlist = [guest["name"] for guest in guests if guest["age"] >= 21 and guest["code"] 
             == PASS_CODE and guest["name"] not in blacklist]

print(guestlist)