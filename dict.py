# info={

#     "key":"value",
#     "name": "Ali",
#     "subjects":["C","C++","Java","Python"],
#     "topics":["Dictionary","Sets"],
#     "age":22,
#     "is_adult":True,
#     "marks": 76.3,
#     2025:2026 # we won't go in this depth complexity, we will go with tuples for keys, or for those which  won't be changed and fixed
# }
# print(info)

# # To access values of dictionary
# print(info["name"])
# print(info[2025])
# print(info["age"])
# # print(info["surname"]) // can only access the  indices or keys which exist

# # For modification
# info["name"]="Ahmad"
# print(info)

# null_dict={}
# null_dict["name"]="Sajid"
# null_dict["age"]=53

# print(null_dict)


# # Nested Dictionaries
# student={
#     "name":"Ahmer",
#     "subjects" :{
#         "Eng":56,
#         "Math" :45,
#         "Chem":54
#     },
#     "age": 21,
# }
# print(student)   #For complete student dictioanry
# print(student["subjects"])   #For Fetching only subjects dictionary | which is the inner dictionary
# print(student["subjects"] ["Eng"]) # For fetching a key: value pair frokkm inner dictioanry

# student2={
#     "name":"Ahmer",
#     "subjects" :{
#         "Eng":56,
#         "Math" :45,
#         "Chem":54
#     },
#     "age": 21,
# }
# # This is how we can update our current dictionary
# new_dict={"city":"Vehari", "age":"23"}
# student2.update(new_dict)
# print(student2)
# # Dictionary methods
# print(student2.keys())  #Only outer keys not the nested nested ones
# print(student2.values())   #Return all values
# print(student2.items())    #Return all key: value pairs as tuple
# print(len(student2))   

# pairs= list(student2.items())
# print(pairs[0]) 
# # To Convert Students dictionary to list
# print(list(student2.keys()))
# print(student2.get())  #Returns the key according to value
# # we can do this without function, but its not a good practice,why?
# # In real time projects, we don't want that error stops working our site or software.
# # SO we will use functions/methods to increase efficiency
 
# Problem 1 Store following word meanings in a python dictionary
dic={
    "table":["a piece of furniture","a list of facts and figures"],
    "cat":"small animal",
}
print(dic)

