tuple1=(1,)    #single element tuple , aftre element comma is necessary
tuple2=(1,2,1,4,2,1,3,2)   #Muli element tuple, okay if put comma after last element but not manadatory

# Tuple Methods

# Index(el) will return the index of first occurence of that element
print(tuple2.index(4))
print(tuple2.index(1))

# count(el)   will count and return the number of occurences of that element
print(tuple2.count(2))
print(tuple2.count(4))


# Problem 1: WAP to count the number of students with the "A" grade in the following tuple
tuple=("C","D","A","A","B","B","A")
print(f"Number of students with A grade are {tuple.count("A")}")

#Problem 2: Store the above values in a list and sort them from "A" to "D"
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)