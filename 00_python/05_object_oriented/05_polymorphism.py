# polymorphism
# poly means many forms 

class Animal :
    def speaks(self):
        print("Generic speaks")

class Dog(Animal) :
    def speaks(self):
        print("Bark")

class Cat(Animal) :
    def speaks(self):
        print("Meow")

class Cow(Animal) :
    def speaks(self):
        print("moooo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speaks()
cat.speaks()
cow.speaks()


# types of polymorphism
# Run time polymorphism
    # method overriding (Ex. animal speaks)
# Compile time polymorphism
    # method overloading (example : two sum functions with different parameters)
    # operator overloading