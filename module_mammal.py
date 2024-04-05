import module_animal
class Mammal(module_animal.Animal):
    def __init__(self, name, specie, weight, predator, little_size):
        super().__init__(name, "Mammal", specie, weight, predator)
        self.little_size = little_size

    def info(self):
        print(f'- {self.name} is a {self.specie}, is a {self.type} and it weights {self.weight} lb. It can have {self.little_size} children.')