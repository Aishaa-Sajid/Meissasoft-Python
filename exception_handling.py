# Basic syntax
# try:
#     num= int(input("Enter a number : "))
#     result=10/num
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Value Error")
# else:
#     print("Result = ",result)
# finally:
#     print("Execution Completed")  
   

class NegativeNumberError(Exception):
    pass
# Catching all execution
# try:
#     num = int(input("Enter number: "))
#     if num < 0:
#         raise NegativeNumberError("Negative numbers are not allowed")
#     print("You entered:", num)
# except NegativeNumberError as e:
#     print("Error:", e)
# print("completed")


# IndexError
# numbers = [10, 20, 30]

# try:
#     index = int(input("Enter index: "))
#     print(numbers[index])
# except IndexError:
#     print("Error: Index out of range")


# Missing key in dictionary
dic={
    "name":"ALi",
     "Marks":"90"
} 
try:
    print(dic["grade"])
except:
    print("Error : Key doesn't exist in dictionary")

# Type Error
try:
    result = "10" + 5
except TypeError:
    print("Error: Unsupported operand types")
