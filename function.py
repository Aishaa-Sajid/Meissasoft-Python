# # We use functions to reduce redundency,improve readability, save time

# def sum(a,b):
#     return a+b


# print("Sum of two numbers is ", sum(2,3)) 

# # Function to print average of 3 numbers

# def avg(a,b,c):
#     av=(a+b+c)/3
#     return av

# print("Average of three numbers is ", avg(1,2,3))

# # WAF toconvert USD to pkr
# # def converter(usd):
# #     pkr=usd*250
# #     print("PKR =",pkr)


# # u=int(input("Enter amount "))
# # converter(u)


# def test(a,b=5):   # default must come after non-default
#     pass

def square(x):
    return x*x

nums=[1,2,3,4,5]
result=map(square,nums)

# print(result)
print(list(result))