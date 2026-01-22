class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} make a sound")

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed

    def sound(self):
        print(f"{self.name} barks.")

animal1=Animal("German Animal")
animal1.sound()

dog1=Dog("Buddy","Golden Retriever")
dog1.sound()
print(f"{dog1.name} is a {dog1.breed}" )