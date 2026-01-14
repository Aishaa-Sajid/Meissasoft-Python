# Problem 1 Print numbers from m1 to 100

# i=1
# while i<=100:
#     print(i)
#     i+=1 

# Problem 2 Print numbers from 100 to 1

# j=100
# while j>=1:
#     print(j)
#     j-=1
   
# Problem 3 Print the elements of the following list using a loop
# num_list=[1,4,9,16,25,36,49,64,81,100]

# i=0
# while i< (len(num_list)):
#     print(num_list[i])
#     i+=1

# Problem 4 Print the multiplication table of a number n
# i=1
# n=int(input("Enter a number : "))
# while i<=10 :
#     print(f"{n} * {i} ={n*i}")
#     i+=1

# problem 5 Search for a number x in this tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100,36)
i=0
x=int(input("Enter a number to search : "))

while i < len(tup):
    if(x== tup[i]):
        print(f"Number is at index {i}")
        break
        # continue | Infinite loop
    else:
        print("finding...")
    i+=1
    