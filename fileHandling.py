# f=open("demo.txt","rt") # We can combine files as text and read open by defeault fi we want towrite we canwrite like "rt"
# data=f.read()
# If you read a file and then reading a line,it will give empty space ,because when you  read the file cursor reached at end then it wll read the empty line and return space
# line1=f.readline()
# print(line1) #Here you will see anextra line space which is due to the next  lne character which is not visible but exist when you break to next line
# print(data)
# print(type(data))
# f.close()
# We can specify number of characters we want to read from a file
# data=f.read(5)


# # Also we can write lines
#  "w" --> This wil overwrite the file content
# f=open("demo.txt","w")
# dataa=f.write(" definitely")
# print(dataa)
# f.close()

# But if you want that your file data won't get overwrite and only this new data append at the last then 
# f=open("demo.txt","a")
# new_data=f.write("\tDone")
# print(new_data)
# f.close()

f=open("sample.txt","w")
f.write("Hello My self Ayesha\nNice to Meet you.")
f.write("Thankyou for your consideration")


##########################################################
# problem 1 print number of even number from the file
# count=0
# with open("list.txt","r") as f:
#     data=f.read()
#     print(data)


# new_data=data.split(",")
# print(new_data)

# for val in new_data:
#     if int(val)%2==0 :
#         count+=1

# print("Total Even Numbers :" , count)


# Problem 2 Find the word in the file
word="Hadia"
with open("demo.txt","r") as f:
    dataa=f.read()
    if word in dataa:
        print("Found")
    else:
        print("Not Found")

