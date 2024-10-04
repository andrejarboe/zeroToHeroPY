mylsit = [1,2,3,4,5]

class Sample():
    def __init__(self,) -> None:
        pass
    pass


my_sample = Sample()

print(f"my_sample type: {type(my_sample)}")

class Dog():
    def __init__(self, breed, name, spots) -> None:
        # Attributes
        # We take in the argument
        # assign it using self.attribute_name, make it the same 
        # self.attribute = breed

        self.breed = breed
        self.name = name
        # Expecta bool for spots
        self.spots = spots
        

myDog = Dog(breed='Mut', name='Sammy', spots=False)

print(f"myDog type: {type(myDog)}")
print(f"myDog: {myDog.attribute}")

# *******Part Two******** #
