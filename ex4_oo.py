# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Pets:

    #Class attribute
    
    #Initializer / Instance attributes
    def __init__(self):
        self.dogs = []
    
    def add_pet(self, new_pet):
        self.dogs.append(new_pet)

pets = Pets()

pets.add_Pet(RussellTerrier("Tom", 6))
pets.add_Pet(RussellTerrier("Fletcher", 7))
pets.add_Pet(Dog("Larry", 9))






#dogs = [RussellTerrier("Tom", 6), Bulldog("Fletcher", 7), Bulldog("Larry", 9)]

#pets = Pets(dogs)




