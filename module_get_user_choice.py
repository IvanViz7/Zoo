import module_zoo

zoo = module_zoo.Zoo()

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