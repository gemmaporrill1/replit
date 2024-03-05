# Setup Code
wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}
# Expected Task: Use an f-string to create a profile string that includes the wizard's name, title, and house.

profile_string = f"{wizard['name']}, the {wizard['title']} of {wizard['house']}"
print(profile_string)
