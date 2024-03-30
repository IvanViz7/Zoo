# Towers of Hanoi


## 1. Considerations


#### 1.1 Assumptions
*Zoo is created to help the Zoo owners to administrate it easslier.  *

#### 1.2 Constraints
*The code has not interface, you need a computer no matter what operator system you work with but it should be able to run console programs in Python. There are some functions like send the animals to an habitat that is not available yet, but I'm working on it.*

#### 1.3 System Environment
*It works with MacOS, Windows and Ubuntu in a Python environment.*

## 2. Architecture


#### 2.1 Overview
*"The Zoo" is a management application made to help people who are working in a Zoo, it serves to keep track of the animals, describes their activities, what they eat, how they move, their name.*

#### 2.2 Component Diagrams
*Provide here the diagram and a detailed description of its most valuable parts. There may be multiple diagrams. Include a description for each diagram. Subsections can be used to list components and their descriptions.*

#### 2.3 Class Diagrams
**

#### 2.4 Sequence Diagrams
*Provide here any sequence diagrams. If possible list the use case they contribute to or solve. Provide descriptions if possible.*

#### 2.5 Deployment Diagrams
*Provide here the deployment diagram for the system including any information needed to describe it. Also, include any information needed to describe future scaling of the system.*

#### 2.6 Other Diagrams
*Provide here any additional diagrams and their descriptions in subsections.*

## 3 User Interface Design
*Provide here any user interface mock-ups or templates. Include explanations to describe the screen flow or progression.*

## 4 Appendices and References


#### 4.1 Definitions and Abbreviations
*List here any definitions or abbreviations that could be used to help a new team member understand any jargon that is frequently referenced in the design document.*

#### 4.2 References
*List here any references that can be used to give extra information on a topic found in the design document. These references can be referred to using superscript in the rest of the document.*

class Zoo:
    def __init__ (self):
        self.animals = []
    
    def add_animal(self, animal):
        
        if len(self.animals) < 10:
            self.animals.append(animal)
            print(f'{animal.name} the {animal.specie} now is a Zoo member')
        else:
            print('The Zoo is full')
      
zoo = Zoo()
