import class_habitat
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
            new_habitat = class_habitat.Habitat(name_new_habitat)
            self.add_habitat(new_habitat)
            habitat = new_habitat
        else:
            habitat = self.habitats[habitat_index]
                
        if habitat.is_compatible(animal):
            habitat.add_animal(animal)
            print(f"\n{animal.name} was successfully added to {habitat.name}.")
        else:
            print(f"\nCannot add {animal.name} to {habitat.name}. Incompatible animal types.")
            add_habitat_cause_nocomp = input(f'\nWould you like to add an habitat for {animal.name} (Y/N): ').lower()
            if add_habitat_cause_nocomp == "y":
                name_new_habitat = input('\nEnter the name of the new habitat: ')
                new_habitat = class_habitat.Habitat(name_new_habitat)
                self.add_habitat(new_habitat)
                habitat = new_habitat
                habitat.add_animal(animal)
                print(f"\n{animal.name} was successfully added to {habitat.name}.")
                
    
    def get_user_choice(self):
        while True:
            self.display_info()
            print("\nWhat would you like to add?")
            print("1. Animal")
            print("2. Habitat")
            choice = input("\nEnter your choice (1 or 2): ")
            if choice == "1":
                print("\nWhat type of animal would you like to add?")
                print("1. Reptile")
                print("2. Mammal")
                print("3. Fish")
                animal_type_choice = input("\nEnter your choice (1, 2 or 3): ")
                if animal_type_choice in ["1", "2", "3"]:
                    name = input("\nEnter the name of the animal: ")
                    species = input("\nEnter the species of the animal: ")
                    weight = float(input("\nEnter the weight in lbs of the animal: "))
                    predator = input("\nIs the animal a predator? (Y/N): ").lower() == "y"
                    if animal_type_choice == "1":
                        venomous = input("\nIs the reptile venomous? (Y/N): ").lower() == "y"
                        return choice, name, species, weight, predator, "Reptile", venomous
                    elif animal_type_choice == "2":
                        little_size = int(input("\nEnter the number of puppies: "))
                        return choice, name, species, weight, predator, "Mammal", little_size
                    elif animal_type_choice == "3":
                        return choice, name, species, weight, predator, "Fish", None
                else:
                    print("Invalid choice. Please enter 1, 2 or 3.")
            elif choice == "2":
                return choice, None, None, None, None, None, None
            else:
                print("Invalid choice. Please enter 1 or 2.")
            
    def display_info(self):
        print(f'\nWelcome to Zoo:\n')
        if not self.habitats:
            print("* Empty zoo *")
        else:
            for habitat in self.habitats:
                habitat.display_info()