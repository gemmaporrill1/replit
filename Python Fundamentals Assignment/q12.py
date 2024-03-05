# Setup Code
library = [
    {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
    {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"},
]
# Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.

selected_books = [book for book in library if book["author"] == "Bathilda Bagshot"]
print(selected_books)
