# map --> Apply this function to every element and return result
num=[1,2,3,4,5,6,7,8,9]
added=list(map(lambda x:x**2 ,num))
print(added)

greater_then_four=list(map(lambda x:x>4 ,num))   #[False, False, False, False, True, True, True, True, True] Because its using condition in each iteration and give  a boolean result
print(greater_then_four)

# filter --> Keep elements only if the conditionis true
even=list(filter(lambda x:x%2==0,num))
print(even)

# sorted --> To iterate over and sort
nums=[6,0,3,5,1,9,0]
sorted_num=list(sorted(nums))
reverse_num=list(sorted(nums,key= lambda x:x , reverse=True))
print(reverse_num)
print(sorted_num)