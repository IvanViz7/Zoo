import class_zoo
import class_habitat
import class_animal
import class_reptile
import class_mammal

# Crear el zoo
zoo = class_zoo.Zoo()

# Crear hábitats predeterminados
jungle = class_habitat.Habitat("Jungle", 2)
flock = class_habitat.Habitat("Flock", 2)
marine = class_habitat.Habitat("Marine", 2)

# Añadir los hábitats al zoo
zoo.add_habitat(jungle)
zoo.add_habitat(flock)
zoo.add_habitat(marine)

# Crear animales predeterminados
default_reptile = class_reptile.Reptile("Coco", "Lizard", 500.0, True, False)
default_mammal = class_mammal.Mammal("Tonio", "Tiger", 200.0, True, 3)
default_fish = class_animal.Animal("Nemo", "Fish", "Clown", 1.0, False)

# Añadir los animales a los hábitats correspondientes
jungle.add_animal(default_reptile)
flock.add_animal(default_mammal)
marine.add_animal(default_fish)

while True:
    user_choice, name, species, weight, predator, animal_type, additional_info = zoo.get_user_choice()
    if user_choice == "1":
        if animal_type == "Reptile":
            new_animal = class_reptile.Reptile(name, species, weight, predator, additional_info)
        elif animal_type == "Mammal":
            new_animal = class_mammal.Mammal(name, species, weight, predator, additional_info)
        else:
            new_animal = class_animal.Animal(name, "Fish", species, weight, predator)
        zoo.add_animal(new_animal)
    elif user_choice == "2":
        habitat_name = input("Enter the name of the habitat: ")
        capacity = int(input('\nEnter the capacity of the new habitat: '))
        new_habitat = class_habitat.Habitat(habitat_name, capacity)
        zoo.add_habitat(new_habitat)
    
    another_action = input("\nDo you want to add another animal or habitat? (Y/N): ")
    if another_action.lower() != "y":
        break
    
print("\nThe Zoo was formed this way:\n")
zoo.display_info()