import copy

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Marceline", "German Shepherd")
dog2 = copy.deepcopy(dog1)
dog2.name = "Cajun"
dog2.breed = "Belgian Malinois"

print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)