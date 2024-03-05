# Setup Code
# Expected Task: Define a `PotionError` exception and use it in a potion-making function.
class PotionError(Exception):
    def __init__(self, ingredient, potion_name):
        self.ingredient = ingredient
        self.potion_name = potion_name


input_ingredient = input("Choose your ingredient: ")


def make_potion(ingredient, potion_name):
    valid_ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]

    try:
        if ingredient not in valid_ingredients:
            raise PotionError(ingredient, potion_name)
    except PotionError as e:
        print(f"{ingredient} is not a valid ingredient for the {potion_name}.")
        return str(e)

    return f"{potion_name} successfully made with {ingredient}!"


print(make_potion(input_ingredient, "Love potion"))
