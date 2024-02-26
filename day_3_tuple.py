#tuple vs list

#tuple = imutable | list = mutable

person = ("Alex", "SA", 20)

print(person, type(person))

#changing a value in a list, can't change in a tuple 
# person[0] = "Thato"

print(person.count(20)) #finds occurences

print(person.index("Alex")) # gets index

# print(person.index(80)) 
# index errors if not found | find gives -1

# not available in tuple | append insert remove pop