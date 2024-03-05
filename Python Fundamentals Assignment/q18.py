# Setup Code
ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
potions = ["Visibility", "Dreaming", "Levetating"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.

for i in range(len(ingredients)):
    for j in range(i + 1, len(ingredients)):
        ingredient1 = ingredients[i]
        ingredient2 = ingredients[j]
        potion = potions[(i + j) % len(potions)]
        print(f"Combining {ingredient1} and {ingredient2} produces a {potion} Potion.")
