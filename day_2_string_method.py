#string methods

# methods to change the case of a string

msg = "Hi, all"
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())

# methods for formatting
quote = "This too shall pass----"
print(quote.strip())
print(quote.strip("-"))
print(quote.lstrip())
print(quote.rstrip())

# methods for searching
print(quote.find("shall")) #returns index of the first match
print(quote.find("*")) #returns -1 if not found

print(quote.replace("shall", "will")) #replacing all occurences, strings are imutable
print(quote) # doesn't change the original string

print(quote.count("l")) # how many times it is replaced, case sensitive

print(quote.startswith("This")) #true
print(quote.endswith("this")) #false

badge_no = "123"
print(badge_no.isdigit()) # true if all digits

name = "Gemma"
print(len(name)) #length of the string