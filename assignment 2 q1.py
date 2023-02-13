#Q1 Write a Python program to get a list, sorted in increasing order by the last element in each tuple 
# from a given list of non-empty tuples ?

def Sort_Tuple(tuple): 
       
    # getting length of list of tuples
    a = len(tuple) 
    for i in range(0, a): 
           
        for j in range(0, a-i-1): 
            if (tuple[j][-1] > tuple[j + 1][-1]): 
                temp = tuple[j] 
                tuple[j]= tuple[j + 1] 
                tuple[j + 1]= temp 
    return tuple
   
tup =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
         
print(Sort_Tuple(tup))

#List

#List are mutable,Iterations are time-consuming,Inserting and deleting items is easier with a list,
#Lists consume more memory,list have several built in function,
# A unexpected change or error is more likely to occur in a list.
#Tuples

#Tuples are immutable,Iterations are comparatively Faster,Accessing the elements is best accomplished with a tuple data type.
#Tuple consumes less than the list,A tuple does not have many built-in methods because of immutability
#In a tuple, changes and errors don't usually occur because of immutability.