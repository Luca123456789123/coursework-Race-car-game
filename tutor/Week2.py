class Animal:
    def __init__(self, species):
         self.species = species
    def display_details(self):
        print(f"Species: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed, age, species):
        super().__init__(species)
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof")

    def display_details(self):
        print(f"Species: {self.species}, Breed: {self.breed}, Name: {self.name}")

my_dog = Dog(species="k9",name="Jeff", breed="pug", age="1" )

my_dog.bark()

print(f"My dog is a {my_dog.species}")

my_dog.display_details()

# Person exercise
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"hi my name is {self.name}")

person1 = Person("luca", "4", "penguin")
person1.introduce()
