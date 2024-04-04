import module_zoo
import module_habitat
import module_animal
import module_get_user_choice
        
zoo = module_zoo.Zoo()
zoo.add_habitat(module_habitat.Habitat("Jungle"))
zoo.add_habitat(module_habitat.Habitat("Flock"))
zoo.add_habitat(module_habitat.Habitat("Forest"))

while True:
    user_choice, animal_type, name, species, weight = module_get_user_choice.get_user_choice()
    if user_choice == "1":
        new_animal = module_animal.Animal(name, animal_type, species, weight)
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
