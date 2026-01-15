# # Set is unordered and unique,will ignore duplicate entries even if you write
# # Note: Sest are mutable but their elements are immutable
# set1={1,2,3,4,"Ali","Chem",4,"A","Pen","world","world"}
# # print(type(set1))
# # print(set1)
# # print(len(set1)) #Even length will ignore duplicates in sets

# # To create empty set
# set2=set()   

# # To add an element
# set2.add("Vehari")
# set2.add((1,2,3))
# set2.add("A")
# set2.add(4)
# set2.add("B")

# # To remove an element
# set2.remove("Vehari")

# To remove a random value
# print(set2.pop())
# Unhashable type(List, Dictionary),will not accepted by sets
# The values which are immutable,their hashvalue can be made
# Set will only accept hashable values

# To empties an element
# coll_set.clear()
# print(len(set2))
# print(set2)

# # combines both set values & return new
# print(set1.union(set2))

# # Combines common values and return new
# print(set1.intersection(set2))

new_set={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(new_set))

# output will be {9}, because python consider 9.0 and 9 same
value={9,"9.0"} # 1st possible solution
# we will use tuple pairs| 2nd solution
values={("float",9.0), ("int",9)}
print(values)

print(value)