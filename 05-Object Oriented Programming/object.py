mylsit = [1,2,3,4,5]

class Sample():
    def __init__(self,) -> None:
        pass
    pass


my_sample = Sample()

print(f"my_sample type: {type(my_sample)}")

class Dog():
    # Class object attribute
    # Same for any instance of a class
    species = 'mammal' 

    def __init__(self, breed, name, spots):
        # Attributes
        # We take in the argument
        # assign it using self.attribute_name, make it the same 
        # self.attribute = breed

        self.breed = breed
        self.name = name
        # Expecta bool for spots
        self.spots = spots
    
    # OPERATIONS/ACTION ---> Methods
    def bark(self, number):
        print(f"Woof! my name is {self.name}, and the number is {number}")
        

myDog = Dog(breed='Mut', name='Samson', spots=False)

print(f"myDog type: {type(myDog)}")
print(f"myDog: {myDog.name}")
print(f"myDog: {myDog.species}")
# print(f"{myDog.bark(number = 9)}")
myDog.bark(9)

# *******Part Two******** #
class Circle():
    # Class Object Attribute
    pi = 3.14
    def __init__(self, radius=1) -> None:
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * Circle.pi * 2

myCircle = Circle(30)
print(f"{myCircle.pi}")
print(f"{myCircle.radius}")
print(f"{myCircle.getCircumference()}")


# ******* Inheritance and Polymorphism******** #
class Animal():
    def __init__(self):
        print("ANIMAL CREATED ")
    
    def whoAmI(self):
        print("I am and animal")
    
    def eat(self):
        print("I am eating")
    
class Dog2(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    def whoAmI(self):
        print("I am a dog")

myDog2 = Dog2()
# print(f"{}")
myDog2.eat()
myDog2.whoAmI()