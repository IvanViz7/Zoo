class Zoo:
    def __init__(self):
        self.habitats = []
    
    def add_habitat(self, habitat):
        self.habitats.append(habitat)
    
    def add_animal(self, animal):
        while True:
            print("\nSelect a habitat to add the animal to:")
            for i, habitat in enumerate(self.habitats):
                print(f"{i+1}. {habitat.name}")
            habitat_index = int(input("\nEnter the habitat number: ")) - 1
            habitat = self.habitats[habitat_index]
            if habitat.is_compatible(animal):
                habitat.add_animal(animal)
                print(f"\n{animal.name} was successfully added to {habitat.name}.")
                break
            else:
                print(f"\nCannot add {animal.name} to {habitat.name}. Incompatible animal types.")
    
    def display_info(self):
        print(f'\nWelcome to Zoo:\n')
        if not self.habitats:
            print("* Empty zoo *")
        else:
            for habitat in self.habitats:
                habitat.display_info()