class Habitat:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.animals = []
    
    def add_animal(self, animal):   
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
            print(f"{animal.name} was successfully added to {self.name}.")
        else:
            print(f"Cannot add {animal.name} to {self.name}. Habitat is full.")
        
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
        print(f'Capacity: {self.capacity}')
        if not self.animals:
            print("No animals in this habitat.")
        else:
            print(f'Animals:')
            for animal in self.animals:
                animal.info()
        print(f'\n')