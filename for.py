# nums=[1,4,9,16,25,36,49,64,81,100]

# # for val in nums:
# #     print(val)

# num_tup=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter number to find in the tuple : "))

# idx=0
# for n in nums:
#     if n == x :
#         print("Number found at index ",idx)
#         break
#     idx+=1
# else:
#     print("Not found")

# Pass statement
# Pass is a null statement that does nothing. It is used as a placeholder for future code
# For example we need to creat a loop and we don't want to do and work in it, we use pass
# If we won't use it then error will be generated that indentation expected an indented block

for i in range(5):
    pass      #skip but different from continue, it says I don't need to do anything yet,may be I will do in future

# Generally pass will used in exceptions and try catch block


# print("some useful work")

# Problem 1 Print multiplication of number n
# n=int(input("Enter your number: "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# Problem 2 WAP to find the sum of first n numbers
n=5
i=1
sum=0
while i<=n:
    sum+=i
    i+=1

print(sum)

# Problem 3 Find the factorial of first n numbers

n=5
fact=1
for i in range(1,n+1):
    fact*=i
    
print(f"Factorial of number {n} is {fact}")
