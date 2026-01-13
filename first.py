# Negative slicing

str1="Hello Meissasoft"
print(str1)
print(str1[1:4])

str="World"
print(str[-5:-2])
print(str[:-2])
print(str[-2:-1])

# String Functions
str2="i am studying Python, flow on on on "
print(str2.endswith("of"))
print(str2.capitalize()) #will capitalize first character of first word
print(str2.replace("on","off"))  #create new string then make changes,won't alter the original string
print(str2)
print(str2.find("i"))
print(str2.count("on"))

name=input("Enter your first name : ")
print(len(name))
name="Ali$Ah$mad"
print(name.find("$"))
print(name.count("$"))

