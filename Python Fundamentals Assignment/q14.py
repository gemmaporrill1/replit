# Setup Code
# Expected Task: Create a base class `MagicalCreature` and subclasses `Dragon`, `Unicorn`. Each subclass should have a unique `sound` method.
class MagicalCreature:
    def __init__(self, noise):
        self.noise = noise

    def sound(self):
        return self.noise


class Dragon(MagicalCreature):
    def __init__(self):
        super().__init__("Roar")


class Unicorn(MagicalCreature):
    def __init__(self):
        super().__init__("Neigh")


dragon = Dragon()
unicorn = Unicorn()

print(
    f"Calling sound() on a Dragon prints '{dragon.sound()}', on a Unicorn prints '{unicorn.sound()}'."
)
