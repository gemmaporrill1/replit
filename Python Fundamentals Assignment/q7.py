# Setup Code
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.

sorted_spells = sorted(spells, key=lambda spell: spell[1], reverse=True)

print(sorted_spells)
