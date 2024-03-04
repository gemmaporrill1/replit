# Setup Code
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.

grams = list(map(lambda ingredient: ingredient + ": 3 grams", ingredients))

print(grams)
