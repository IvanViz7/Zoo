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
        
zoo = []
listchoice =[]
        
class Lion(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is running')
    
    def eat(self):
        print(f'{self.name} is eating meat')
        
class Monkey(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is jumping between ropes')
    
    def eat(self):
        print(f'{self.name} is eating fleas')

class Iguana(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is running over the water')
    
    def eat(self):
        print(f'{self.name} is eating vegetables and fruits')

class Crocodile(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is swimming in the water')
    
    def eat(self):
        print(f'{self.name} is eating meat')
        
class Zebra(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is jumping in the field')
    
    def eat(self):
        print(f'{self.name} is eating grass')

class Giraffe(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is running around the field')
    
    def eat(self):
        print(f'{self.name} is eating grass from the trees')
        
class Turtle(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is sleeping in its shell')
    
    def eat(self):
        print(f'{self.name} is eating seaweed and shrimp')
        
class Hippo(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is taking a shower in the lake')
    
    def eat(self):
        print(f'{self.name} is eating lettuce')
        
class Python(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is trying to hide in its cave')
    
    def eat(self):
        print(f'{self.name} is eating meat')
        
class Tigger(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is running too quickly')
    
    def eat(self):
        print(f'{self.name} is eating meat')

lion = Lion('Jackson', 'Mammal', 'Lion', 600)
monkey = Monkey('Lisa', 'Mammal', 'Monkey', 80)
iguana = Iguana('Iguanol', 'Reptile', 'Iguana', 6)
crocodile = Crocodile('Pancho', 'Reptile', 'Crocodile', 450)
zebra = Zebra('Marty', 'Mammal', 'Zebra', 700)
giraffe = Giraffe('Melman', 'Mammal', 'Giraffe', 1000)
turtle = Turtle('Leonardo', 'Reptile', 'Turtle', 800)
hippo = Hippo('Maria', 'Mammal', 'Hippo', 1800)
python = Python('Pedro', 'Reptile', 'Snake', 30)
tigger = Tigger('Gatito', 'Mammal', 'Tigger', 450)

def add_animal(animal):
    zoo.append(animal)
    animals_zoo=len(zoo)
    if(animals_zoo < 10):
        print(f"{animal.name} the {animal.specie} now is a member of our Zoo family")
        animal.info()
        animal.move()
        animal.eat() 

        
while len(zoo) < 10:
    choice = input('Choose a number form 1 to 10 to add an animal to the Zoo: ')
    choice = int(choice)
    newchoice = choice
    
    if choice < 1 or choice > 10:
        print('Invalid character')
    elif newchoice in listchoice:
        print('This animal is already in the Zoo')
    else:
        if(choice == 1):
            animal = lion
            add_animal(animal)
            listchoice.append(newchoice)
        elif(choice == 2):
            animal = monkey
            add_animal(animal)  
            listchoice.append(newchoice)
        elif(choice == 3):
            animal = iguana
            add_animal(animal)            
            listchoice.append(newchoice)
        elif(choice == 4):
            animal = crocodile
            add_animal(animal)
            listchoice.append(newchoice)
        elif(choice == 5):
            animal = giraffe
            add_animal(animal)
            listchoice.append(newchoice)
        elif(choice == 6):
            animal = zebra
            add_animal(animal)
            listchoice.append(newchoice)
        elif(choice == 7):
            animal = turtle
            add_animal(animal)
            listchoice.append(newchoice)
        elif(choice == 8):
            animal = hippo
            add_animal(animal)
            listchoice.append(newchoice)
        elif(choice == 9):
            animal = python
            add_animal(animal)
            listchoice.append(newchoice)
        elif(choice == 10):
            animal = tigger
            add_animal(animal)
            listchoice.append(newchoice)
else:
    print('The Zoo is full')