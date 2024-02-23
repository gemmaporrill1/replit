library_list = [

    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]

#task 1 
#create a function to add a new book to the library
#add_book(library, new_book)

# new_book = {"title": "The Great Gatsby", "author": "F Scott", "year": 1942, "available": True}

# #pass by reference | library and library_list have the same address
# def add_book(library, new_book):
#   library.append(new_book)
#   return library
  
# print(add_book(library_list, new_book))

# # pass by value is more complicated


# #task 2 search(library, author_name)
# #search author and return a []

# def search(library, author_name):
#   books = []
#   for book in library:
#     if book["author"] == author_name:
#       books.append(book)
#   return books

# print(search(library_list, "Mark Lutz"))

# #list comprehension
# def search_by_author(library, author_name):
#   return [ book for book in library if author_name == book["author"]]

# print(search_by_author(library_list, "Mark Lutz"))

#task 3
#check availability
# check out if available 

# chosen_title = input("Which book would you like to check out? ")

# def check_out_book(library, title):
#     for book in library:
#         if book["title"] == title:
#           if book["available"]:
#             print("Check out successful")
#             book["available"] = False 
#             return library
#           else:
#             print("Book is unavailable")
#             return library

# library = check_out_book(library_list, chosen_title)

#Ragav's answer
def check_out_book(library, title):
  for book in library:
    if(book['title'] == title and book['available']):
      book['available'] = False
      return f"Yes, {title} is available and successful check out"

  return f"{title} is unavailable"
      
print(check_out_book(library_list, "Fluent Python"))
# def check_out_book(library, title):
# return [ book for book in library if title == book["title"] 
# and book["available"] == True ]

#dictionary - not a sequence | yes its an iterable