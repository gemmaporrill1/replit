# Setup Code
adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Task: Use `filter` and `map` to create a list of matches between adopters and creatures.

match_list = match_list = list(
    filter(
        lambda adopter_creature: adopter_creature[1]
        in map(lambda creature: creature[1], creatures),
        adopters,
    )
)

print(match_list)
