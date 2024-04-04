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