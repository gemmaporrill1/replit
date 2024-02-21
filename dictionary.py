# Dictionary -> HashMap -> key: Value
# Keys should be unique, can't have a duplicate

# [] | List
# () | Tuple
# {} | Dictionary

person = {
  "name": "Siya Kolisi",
  "age": 32,
  "country": "SA",
  "sport": "Rugby"
}

#access
print(person, type(person))
print(person["name"])

#update
person["age"] += 1 
print(person["age"])

#methods
# Iterable -> list, tuple, dict_keys (can use for loop)
print(person.keys()) #gives key titles
print(person.values()) #gives key values
print(person.items()) #tuple of items -> can use unpacking , using with a for loop

#Looping a dictionary

for detail in person.items():
  print(detail[0]) #[0] gives you just the keys or 1 gives you values

#unpacking a dictionary
for key, value in person.items(): #give proper name
  print(key, value)