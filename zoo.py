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
        print(self.name)
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
        print(f'- {self.name} the {self.specie}, is a {self.type} and it weights {self.weight} lb')
        
zoo = Zoo()
zoo.add_habitat(Habitat("Jungle"))
zoo.add_habitat(Habitat("Flock"))
zoo.add_habitat(Habitat("Forest"))

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
                animal_type = None
                if animal_type_choice == "1":
                    animal_type = "Reptile"
                elif animal_type_choice == "2":
                    animal_type = "Mammal"
                elif animal_type_choice == "3":
                    animal_type = "Fish"
                return choice, animal_type, name, species, weight
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
        elif choice == "2":
            return choice, None, None, None, None
        else:
            print("Invalid choice. Please enter 1 or 2.")

while True:
    user_choice, animal_type, name, species, weight = get_user_choice()
    if user_choice == "1":
        new_animal = Animal(name, animal_type, species, weight)
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
