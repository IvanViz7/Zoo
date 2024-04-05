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

class Animal:
    def __init__(self, name, type, specie, weight, predator):
        self.name = name
        self.type = type
        self.specie = specie
        self.weight = weight
        self.predator = predator
          
    def info(self):
        print(f'- {self.name} is a {self.specie}, is a {self.type} and it weights {self.weight} lb')

class Reptile(Animal):
    def __init__(self, name, specie, weight, predator, venomous):
        super().__init__(name, "Reptile", specie, weight, predator)
        self.venomous = venomous

    def info(self):
        venom_status = "venomous" if self.venomous else "non-venomous"
        print(f'- {self.name} is a {self.specie}, is a {self.type} and it weights {self.weight} lb. It is {venom_status}.')


class Mammal(Animal):
    def __init__(self, name, specie, weight, predator, little_size):
        super().__init__(name, "Mammal", specie, weight, predator)
        self.little_size = little_size

    def info(self):
        print(f'- {self.name} is a {self.specie}, is a {self.type} and it weights {self.weight} lb. It can have {self.little_size} children.')

def get_user_choice():
    while True:
        zoo.display_info()
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
            
# Crear el zoo
zoo = Zoo()

# Crear hábitats predeterminados
jungle = Habitat("Jungle")
flock = Habitat("Flock")
marine = Habitat("Marine")

# Añadir los hábitats al zoo
zoo.add_habitat(jungle)
zoo.add_habitat(flock)
zoo.add_habitat(marine)

# Crear animales predeterminados
default_reptile = Reptile("Coco", "Lizard", 500.0, True, False)
default_mammal = Mammal("Tonio", "Tiger", 200.0, True, 3)
default_fish = Animal("Nemo", "Fish", "Clown", 1.0, False)

# Añadir los animales a los hábitats correspondientes
jungle.add_animal(default_reptile)
flock.add_animal(default_mammal)
marine.add_animal(default_fish)

while True:
    user_choice, name, species, weight, predator, animal_type, additional_info = get_user_choice()
    if user_choice == "1":
        if animal_type == "Reptile":
            new_animal = Reptile(name, species, weight, predator, additional_info)
        elif animal_type == "Mammal":
            new_animal = Mammal(name, species, weight, predator, additional_info)
        else:
            new_animal = Animal(name, "Fish", species, weight, predator)
        zoo.add_animal(new_animal)
    elif user_choice == "2":
        habitat_name = input("Enter the name of the habitat: ")
        new_habitat = Habitat(habitat_name)
        zoo.add_habitat(new_habitat)
    
    another_action = input("\nDo you want to add another animal or habitat? (yes/no): ")
    if another_action.lower() != "yes":
        break
    
print("\nThe Zoo was formed this way:\n")
zoo.display_info()