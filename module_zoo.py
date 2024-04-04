class Zoo:
    def __init__(self):
        self.habitats = []   
    
    def add_habitat(self, habitat):
        self.habitats.append(habitat)
    
    def add_animal(self, animal):
        print("\nSelect a habitat to add the animal to:")
        for i, habitat in enumerate(self.habitats):
            print(f"{i+1}. {habitat.name}")
        habitat_index = int(input("\nEnter the habitat number: ")) - 1
        self.habitats[habitat_index].add_animal(animal)
    
    def display_info(self):
        print(f'\n* * * Welcome to Zoo * * *\n')
        for habitat in self.habitats:
            habitat.display_info()