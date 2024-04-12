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
            capacity = int(input('\nEnter the capacity of the new habitat: '))
            new_habitat = class_habitat.Habitat(name_new_habitat, capacity)
            self.add_habitat(new_habitat)
            habitat = new_habitat
        else:
            habitat = self.habitats[habitat_index]
                
        if len(habitat.animals) < habitat.capacity:
            if habitat.is_compatible(animal):
                habitat.add_animal(animal)
            else:
                print(f"\nCannot add {animal.name} to {habitat.name}. Incompatible animal types.")
        else:
            print(f"\n{habitat.name} is full. Creating a new habitat...")
            name_new_habitat = self.generate_habitat_name(habitat.name)
            new_habitat = class_habitat.Habitat(name_new_habitat, habitat.capacity)
            self.add_habitat(new_habitat)
            new_habitat.add_animal(animal)
            
    def generate_habitat_name(self, base_name):
        count = 2
        new_name = base_name
        if base_name[-1].isdigit():
            while base_name[-1].isdigit():
                base_name = base_name[:-1]
        else:
            base_name += " "
        while any(habitat.name == new_name for habitat in self.habitats):
            new_name = f"{base_name}{count}"
            count += 1
        return new_name
    
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
                    predator = input("\nIs the animal a predator? (yes/no): ").lower() == "yes"
                    if animal_type_choice == "1":
                        venomous = input("\nIs the reptile venomous? (yes/no): ").lower() == "yes"
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
        print(f'\n*** Welcome to Zoo ***\n')
        if not self.habitats:
            print("* Empty zoo *")
        else:
            for habitat in self.habitats:
                habitat.display_info()