# list=[10,20,30,40,50]
# print(list)
# print(type(list))
# print(len(list))
# print(list[0])


# list1=["Ali",12,53, "Abc"]
# print(len(list1))
# print(list1[3])

# #list slicing
# mark_list=[64,54,76,44,98,32,70]
# print(mark_list[1:5])
# print(mark_list[:5])
# print(f"Negative Slicing {mark_list[-5:-1]}")  #format string

# # list operations
# list=[5,1,3,8,0,12,11]

# # To insert an element at end  of a list
# list.append(7)
# print(list)

# #To sort list in ascending order, sort method will return none, it will only make changes in original list
# # list.sort()
# # print(list)

# # To reverse a list ,if already sorted then reverse will gi in decending order, but if not then it will only reverse the string in order it was written
# list.reverse()
# print(list)

# # To insert an element at some particular index | insert(idx, value)
# list.insert(3,20)
# print(list)

# # Sort list in ascending order
# alpha_list=["a","z","f","i","x","q"]
# str_list=["Fig","Cocoa","Mango","Apple"]

# alpha_list.sort()
# print(alpha_list)

# str_list.sort()
# print(str_list)

# # Sort list in decending order, 
# # WHy we are putting  reverse argument in sort as it returns none,
# # Because sort is defined like this it reverse is predefined argument in sort method with a value set to False
# alpha_list.sort(reverse=True)
# print(alpha_list)

# str_list.sort(reverse=True)
# print(str_list)

# # To remove an element from last index
# list.remove(1)
# print(list)

# new_list=[2,1,3,1]
# # new_list.remove(1)     #Remove first occurence
# # new_list.pop(2)      #Remove element at particular index
# # print(new_list)

# # Count will return the number of occurence of an element
# print(new_list.count(1))

# Problem 1: WAP to ask the user to enter names of their three favourite movies & store them in a list
list=[]

mov=input("Enter the names of your first favourite movies : ")
list.append(mov)

list.append(input("Enter the names of your second favourite movies : "))

mov=input("Enter the names of your third favourite movies : ")
list.append(mov)
print(list)

#Problme 2: WAP to check if a list contains a palindrome of elements
# Palindrome: Things which are same to read from both sides
list=[1,2,3,2,1]
copy_list=list.copy()

copy_list.reverse()

if(list == copy_list):
   print("Yes,Its a palindrome.")
else:
   print("NOt palindrom")   