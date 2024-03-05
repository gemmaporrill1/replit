# Setup Code
# Expected Task: Implement a class with methods for casting spells, reducing health points, and determining the winner.


class WizardDuel:
    def __init__(self, name, initial_health=20):
        self.name = name
        self.health = initial_health

    def spell_casting(self, opponent):
        print(f"{self.name} casts a spell at {opponent.name}")

    def reduce_health(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def determine_winner(self, opponent):
        if self.health > opponent.health:
            return f"{self.name} wins the duel with {self.health} health points left"
        elif self.health < opponent.health:
            return (
                f"{opponent.name} wins the duel with {self.health} health points left"
            )
        else:
            return "It's a draw!"


harry = WizardDuel(name="Harry")
draco = WizardDuel(name="Draco")

harry.spell_casting(draco)

draco.reduce_health(10)

result = harry.determine_winner(draco)
print(result)
