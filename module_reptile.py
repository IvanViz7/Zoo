import module_animal
class Reptile(module_animal.Animal):
    def __init__(self, name, specie, weight, predator, venomous):
        super().__init__(name, "Reptile", specie, weight, predator)
        self.venomous = venomous

    def info(self):
        venom_status = "venomous" if self.venomous else "non-venomous"
        print(f'- {self.name} is a {self.specie}, is a {self.type} and it weights {self.weight} lb. It is {venom_status}.')