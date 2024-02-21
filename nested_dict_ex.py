# #employee array to estimate years of experience

# employees = [
#   {"name": "Alex", "experience": 2},
#   {"name": "Gemma"},
#   {"name": "Rashay", "experience": 4},
#   {"name": "Thato"}
# ]

# #task 1 | task 2 -> get
# #2024 -> +1 year

# years_experience = [(employee.get("experience", 0) + 1) for employee in employees]
# print(years_experience)

# #task 3 print status

# status_levels = [
#   "Junior", "Mid-level", "Senior"
# ]

# for employee in employees:
#   employee["experience"] = employee.get("experience", 0) + 1
#   experience = employee["experience"]
#   if (experience >= 5):
#       print(employee["name"], "is a", status_levels[2])
#   elif (experience >= 3):
#       print(employee["name"], "is a", status_levels[1])
#   else:
#       print(employee["name"], "is a", status_levels[0])


#copy
movie = {
  "name": "Mr Bones",
  "year": 2001
}

movie_copy1 = movie.copy()

#unpacking operator list -> *
# for dictionaries -> **

movie_copy2 = {**movie, "rating": 10}
print(movie_copy2)

movie_copy3 = {**movie, "rating": 10, "year": 2002}
print(movie_copy3)

movie_copy4 = {"rating": 10, "year": 2002, **movie}
print(movie_copy4)

#combining dictionaries
movie = {
  "name": "Mr Bones",
  "year": 2001
}

detail = {
  "actor": "Leon",
  "director": "Dzithendo"
}

movie_details = {**movie, **detail} #preferred
print(movie_details)

price = [100, 1200, 400]
price_copy = [*price]
print(price_copy)

price_copy1 = [50, 40, *price, 60]
print(price_copy1)

t1 = [80, 90]
t2 = [50, 60]

t3 = [*t1, *t2] #preferred
print(t3)