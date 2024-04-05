import module_habitat
class Zoo:
    def __init__(self):
        self.habitats = []
    
    def add_habitat(self, habitat):
        self.habitats.append(habitat)
    
    def add_animal(self, animal):
        print("\nSelect a habitat to add the animal to:")
        for i, habitat in enumerate(self.habitats):
            print(f"{i+1}. {habitat.name}")
        print(f"{len(self.habitats) + 1}. Add a new habitat")

        habitat_index = int(input("\nEnter the habitat number: ")) - 1

        if habitat_index == len(self.habitats):
            name_new_habitat = input('\nEnter the name of the new habitat: ')
            new_habitat = module_habitat.Habitat(name_new_habitat)
            self.add_habitat(new_habitat)
            habitat = new_habitat
        else:
            habitat = self.habitats[habitat_index]
                
        if habitat.is_compatible(animal):
            habitat.add_animal(animal)
            print(f"\n{habitat.name} was added to the Zoo")
            print(f"\n{animal.name} was successfully added to {habitat.name}.")
        else:
            print(f"\nCannot add {animal.name} to {habitat.name}. Incompatible animal types.")
    
    def display_info(self):
        print(f'\nWelcome to Zoo:\n')
        if not self.habitats:
            print("* Empty zoo *")
        else:
            for habitat in self.habitats:
                habitat.display_info()