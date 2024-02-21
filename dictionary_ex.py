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
#   book_list.append(dictionary)
#   if dictionary["rating"] >= 4.7:
#     print(dictionary["title"])

#task 2 : list comprehension

# book_list = [dictionary["title"] for dictionary in books if dictionary["rating"] >= 4.7]
# print(book_list)

#task 3 
#A-Z order

book_list = [dictionary["title"] for dictionary in books if dictionary["rating"] >= 4.7]
# book_list.sort() #mutation happens
print(sorted(book_list)) #sorts it and provides copy
