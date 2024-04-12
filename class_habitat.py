class Habitat:
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal):   
        self.animals.append(animal)
        
    def is_compatible(self, new_animal):
        if not self.animals:
            return True
        animal_types = set([animal.type for animal in self.animals])
        if new_animal.type not in animal_types:
            return False
        predators = set([animal.predator for animal in self.animals])
        return new_animal.predator in predators
    
    def display_info(self):
        print(f'Habitat: {self.name}')
        for animal in self.animals:
            animal.info()