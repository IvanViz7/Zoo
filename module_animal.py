class Animal:
    def __init__(self, name, type, specie, weight, predator):
        self.name = name
        self.type = type
        self.specie = specie
        self.weight = weight
        self.predator = predator
          
    def info(self):
        print(f'- {self.name} is a {self.specie}, is a {self.type} and it weights {self.weight} lb')