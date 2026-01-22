# Parent class 1
class Father:
    def skills(self):
        print("Father has programming skills.")

# Parent class 2
class Mother:
    def hobbies(self):
        print("Mother loves painting.")

# Child class inherits from both Father and Mother
class Child(Father, Mother):
    def sports(self):
        print("Child loves football.")

# Create object of Child
c1 = Child()
c1.skills()    # From Father
c1.hobbies()   # From Mother
c1.sports()    # From Child itself
