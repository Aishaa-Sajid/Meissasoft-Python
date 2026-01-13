#Problem 1: If the number is even or odd

# num=int(input("Enter your Number : "))

# if(num<0):
#      print("Invalid number")
# elif(num%2 == 0):
#      print("Even NUmber")
# elif(num%2 == 1):
#     print("Odd Number")
# else:
#     print("Good to go")

# Problem 2: Is the nUmber multiplication of 7
# if(num%7==0):
#     print("congratulations Number is multiple of 7")
# else:
#     print("Number is not multiple of 7")    

# Problem 3: Find the greatest Number

# a=int(input("Enter 1st number : "))
# b=int(input("Enter 2nd number : "))
# c=int(input("Enter 3rd number : "))

# if(a>b and a>c):
#        max=a
# elif(b>c):
#         max=b
# else:
#         max=c


# print("Maximum number is :" , max)  


st="Hello Welcome Thankyou"
result=st.split()   #['Hello', 'Welcome', 'Thankyou'] | splits the string at spaces by default.
print(result)

s = "one two three four five six seven eight nine"
result = s.split(" ",5)
print(result)