import module_zoo
import module_habitat
import module_animal
import module_reptile
import module_mammal

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
zoo = module_zoo.Zoo()

# Crear hábitats predeterminados
jungle = module_habitat.Habitat("Jungle")
flock = module_habitat.Habitat("Flock")
marine = module_habitat.Habitat("Marine")

# Añadir los hábitats al zoo
zoo.add_habitat(jungle)
zoo.add_habitat(flock)
zoo.add_habitat(marine)

# Crear animales predeterminados
default_reptile = module_reptile.Reptile("Coco", "Lizard", 500.0, True, False)
default_mammal = module_mammal.Mammal("Tonio", "Tiger", 200.0, True, 3)
default_fish = module_animal.Animal("Nemo", "Fish", "Clown", 1.0, False)

# Añadir los animales a los hábitats correspondientes
jungle.add_animal(default_reptile)
flock.add_animal(default_mammal)
marine.add_animal(default_fish)

while True:
    user_choice, name, species, weight, predator, animal_type, additional_info = get_user_choice()
    if user_choice == "1":
        if animal_type == "Reptile":
            new_animal = module_reptile.Reptile(name, species, weight, predator, additional_info)
        elif animal_type == "Mammal":
            new_animal = module_mammal.Mammal(name, species, weight, predator, additional_info)
        else:
            new_animal = module_animal.Animal(name, "Fish", species, weight, predator)
        zoo.add_animal(new_animal)
    elif user_choice == "2":
        habitat_name = input("Enter the name of the habitat: ")
        new_habitat = module_habitat.Habitat(habitat_name)
        zoo.add_habitat(new_habitat)
    
    another_action = input("\nDo you want to add another animal or habitat? (yes/no): ")
    if another_action.lower() != "yes":
        break
    
print("\nThe Zoo was formed this way:\n")
zoo.display_info()