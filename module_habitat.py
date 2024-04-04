class Habitat:
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal):   
        self.animals.append(animal)
    
    def display_info(self):
        print(self.name)
        for animal in self.animals:
            animal.info()