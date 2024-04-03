class Zoo:
    def __init__(self):
        self.habitats = []
    
    def add_habitat(self, habitat):
        self.habitats.append(habitat)
    
    def add_animal(self, animal):
        print("Select a habitat to add the animal to:")
        for i, habitat in enumerate(self.habitats):
            print(f"{i+1}. {habitat.name}")
        habitat_index = int(input("Enter the habitat number: ")) - 1
        self.habitats[habitat_index].add_animal(animal)
    
    def display_info(self):
        print(f'Guadalajara Zoo:')
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
    
    def display_info(self):
        print(f'Habitat: {self.name}')
        for animal in self.animals:
            animal.info()

class Animal:
    def __init__(self, name, type, specie, weight):
        self.name = name
        self.type = type
        self.specie = specie
        self.weight = weight
    
    def move(self):
        pass
    
    def eat(self):
        pass  
          
    def info(self):
        print(f'The name of the {self.specie} is {self.name}, {self.name} is a {self.type} and it weights {self.weight} lb')
        
zoo = Zoo()

def get_user_choice():
    while True:
        zoo.display_info()
        print("What would you like to add?")
        print("1. Animal")
        print("2. Habitat")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            while True:
                print("What type of animal would you like to add?")
                print("1. Reptile")
                print("2. Mammal")
                print("3. Fish")
                animal_type_choice = input("Enter your choice (1, 2 or 3): ")
                if animal_type_choice in ["1", "2", "3"]:
                    return choice, animal_type_choice
                else:
                    print("Invalid choice. Please enter 1, 2 or 3.")
        elif choice == "2":
            return choice, None
        else:
            print("Invalid choice. Please enter 1 or 2.")

while True:
    user_choice = get_user_choice()
    if user_choice == "1":
        name = input("Enter the name of the animal: ")
        animal_type = input("Enter the type of the animal: ")
        species = input("Enter the species of the animal: ")
        weight = float(input("Enter the weight of the animal: "))
        new_animal = Animal(name, animal_type, species, weight)
        zoo.add_animal(new_animal)
    elif user_choice == "2":
        habitat_name = input("Enter the name of the habitat: ")
        new_habitat = Habitat(habitat_name)
        zoo.add_habitat(new_habitat)
    
    another_action = input("Do you want to add another animal or habitat? (yes/no): ")
    if another_action.lower() != "yes":
        break

zoo.display_info()